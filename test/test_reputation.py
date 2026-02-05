import re

import synapse.tests.utils as s_t_utils
from aioresponses import aioresponses
from synapse.tools import genpkg

from .common import BASE_URL, SYNAPSE_PACKAGE_YAML, get_mock_file_content


class TestReputation(s_t_utils.SynTest):
    @aioresponses()
    async def test_fqdn_reputation(self, mocked: aioresponses):
        mocked.get(
            re.compile(
                f"^{re.escape(BASE_URL + 'axon/domain/reputation/quick/' + 'google.com')}"
            ),
            status=200,
            body=get_mock_file_content(
                "axon_domain_reputation_quick_google.com.json"
            ),
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            with self.getAsyncLoggerStream("synapse.storm.log"):

                # Run the storm command to trigger reputation check
                await core.callStorm("[inet:fqdn=google.com] | s1.validin.reputation")

                mocked.assert_called()

                # Assert meta:source exists
                metasource_iden = await core.callStorm(
                    'meta:source:name="validin api" | return($node.repr())'
                )
                assert metasource_iden, "Find metasource node"

                # Assert rank properties are set
                majestic = await core.callStorm(
                    'inet:fqdn=google.com | return($node.props."_s1:validin:rank:majestic")'
                )
                assert majestic == 2, "Majestic rank should be 2"

                tranco = await core.callStorm(
                    'inet:fqdn=google.com | return($node.props."_s1:validin:rank:tranco")'
                )
                assert tranco == 1, "Tranco rank should be 1"

                umbrella = await core.callStorm(
                    'inet:fqdn=google.com | return($node.props."_s1:validin:rank:umbrella")'
                )
                assert umbrella == 1, "Umbrella rank should be 1"

                anchors = await core.callStorm(
                    'inet:fqdn=google.com | return($node.props."_s1:validin:rank:anchors")'
                )
                assert anchors == 8, "Anchors rank should be 8"

                # Assert node data is stored
                data = await core.callStorm(
                    'inet:fqdn=google.com | return($node.data.get(s1:validin:reputation))'
                )
                assert data is not None, "Raw reputation data should be stored"
                assert data.get("score") == 1.4, "Score should be 1.4"

    @aioresponses()
    async def test_ipv4_reputation(self, mocked: aioresponses):
        mocked.get(
            re.compile(
                f"^{re.escape(BASE_URL + 'axon/ip/reputation/quick/' '1.1.1.1')}"
            ),
            status=200,
            body=get_mock_file_content(
                "axon_ip_reputation_quick_1.1.1.1.json"
            ),
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            
            # Ensure model extensions are loaded (onload should do this, but test env may need explicit call)
            try:
                await core.callStorm("$lib.import(s1.validin.model).update_forms()")
            except Exception:
                pass  # Ignore if already loaded
            
            with self.getAsyncLoggerStream("synapse.storm.log") as stream:
                # Run the storm command
                msgs = await core.stormlist("[inet:ipv4=1.1.1.1] | s1.validin.reputation")
                
                # Print all messages to see errors/warnings
                for msg in msgs:
                    if msg[0] in ('warn', 'err'):
                        print(f"Storm {msg[0]}: {msg[1]}")

                mocked.assert_called()

                # Assert meta:source exists
                metasource_iden = await core.callStorm(
                    'meta:source:name="validin api" | return($node.repr())'
                )
                assert metasource_iden, "Find metasource node"

                # Assert rank properties 
                
                pivot_count = await core.callStorm(
                    'inet:ipv4=1.1.1.1 | return($node.props."_s1:validin:rank:pivot_count")'
                )
                assert pivot_count == 2213460, "Pivot count should be 2213460"

                top_a = await core.callStorm(
                    'inet:ipv4=1.1.1.1 | return($node.props."_s1:validin:rank:top_a")'
                )
                assert top_a == 3220, "Top A rank should be 3220"

                # Assert ASN node created
                asn_count = await core.count("inet:asn=13335")
                assert asn_count == 1, "ASN node should be created"

                # Assert ASN linked to IP
                asn = await core.callStorm(
                    'inet:ipv4=1.1.1.1 | return($node.props.asn)'
                )
                assert asn == 13335, "ASN should be 13335"

                # Assert ASN name
                asn_name = await core.callStorm(
                    'inet:asn=13335 | return($node.props.name)'
                )
                assert asn_name == "cloudflarenet", "ASN name should be cloudflarenet"

                # Assert location
                latlong = await core.callStorm(
                    'inet:ipv4=1.1.1.1 | return($node.props.latlong)'
                )
                assert latlong is not None, "Latlong should be set"
                assert latlong[0] == -33.8688, "Latitude should be -33.8688"
                assert latlong[1] == 151.209, "Longitude should be 151.209"

                loc = await core.callStorm(
                    'inet:ipv4=1.1.1.1 | return($node.props.loc)'
                )
                assert loc == "au", "Location should be AU"

                # Assert node data is stored
                data = await core.callStorm(
                    'inet:ipv4=1.1.1.1 | return($node.data.get(s1:validin:reputation))'
                )
                assert data is not None, "Raw reputation data should be stored"

    @aioresponses()
    async def test_malicious_domain(self, mocked: aioresponses):
        mocked.get(
            re.compile(
                f"^{re.escape(BASE_URL + 'axon/domain/reputation/quick/' + 'micsrosoftonline.com')}"
            ),
            status=200,
            body=get_mock_file_content(
                "axon_domain_reputation_quick_micsrosoftonline.com.json"
            ),
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            with self.getAsyncLoggerStream("synapse.storm.log"):

                # Run the storm command
                await core.callStorm("[inet:fqdn=micsrosoftonline.com] | s1.validin.reputation")

                mocked.assert_called()

                # Assert meta:source exists
                metasource_iden = await core.callStorm(
                    'meta:source:name="validin api" | return($node.repr())'
                )
                assert metasource_iden, "Find metasource node"

                # Assert node data is stored even without rank annotations
                data = await core.callStorm(
                    'inet:fqdn=micsrosoftonline.com | return($node.data.get(s1:validin:reputation))'
                )
                assert data is not None, "Raw reputation data should be stored"

                # Verify command handles missing rank annotations gracefully
                # (no properties should be set, but no errors should occur)
                majestic = await core.callStorm(
                    'inet:fqdn=micsrosoftonline.com | return($node.props."_s1:validin:rank:majestic")'
                )
                assert majestic is None, "Majestic rank should be None for malicious domain"
