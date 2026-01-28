import re

import synapse.tests.utils as s_t_utils
from aioresponses import aioresponses
from synapse.tools import genpkg

from .common import BASE_URL, SYNAPSE_PACKAGE_YAML, get_mock_file_content


class TestCTStream(s_t_utils.SynTest):
    @aioresponses()
    async def test_ctstream(self, mocked: aioresponses):
        mocked.get(
            re.compile(
                f"^{re.escape(BASE_URL + 'axon/domain/certificates/' + 'github.com')}"
            ),
            status=200,
            body=get_mock_file_content(
                "axon_domain_certificates_github.com.json"
            ),
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            with self.getAsyncLoggerStream("synapse.storm.log"):
                await core.callStorm("[inet:fqdn=github.com] | s1.validin.certs")

                metasource_iden = await core.callStorm(
                    'meta:source:name="validin api" | return($node.repr())'
                )
                assert metasource_iden, "Find metasource node"

                count = await core.count("crypto:x509:cert")
                assert count == 26, "Count of crypto:x509:cert nodes should be 26"

                cert_with_sha256 = await core.callStorm(
                    'crypto:x509:cert:sha256="09010cce9b722155c7e686b07739d3d2dc0605dea1a4984a0b965e18777726b5" | return($node.repr())'
                )
                assert cert_with_sha256, "Find cert with sha256 fingerprint"

                count = await core.count("inet:fqdn")
                assert count > 1, "Should have multiple inet:fqdn nodes from certificate domains"
