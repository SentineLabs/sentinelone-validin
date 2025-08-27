import re
import synapse.tests.utils as s_t_utils
from synapse.tools import genpkg
from aioresponses import aioresponses

from .common import get_mock_file_content, BASE_URL, SYNAPSE_PACKAGE_YAML

class TestEnrich(s_t_utils.SynTest):

    @aioresponses()
    async def test_fqdn_enrich(self, mocked: aioresponses):
        mocked.get(
            re.compile(f'^{re.escape(BASE_URL + 'v2/domain/combined/connections/'+'validin.com')}'),
            status=200,
            body=get_mock_file_content('v2_domain_combined_connections_validin.com.json')
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            with self.getAsyncLoggerStream('synapse.storm.log') as stream:
                # Run the storm command to trigger the crawl
                await core.callStorm('[inet:fqdn=validin.com] | s1.validin.enrich')

                metasource_iden = await core.callStorm('meta:source:name="validin api" | return($node.repr())')
                assert metasource_iden, "Find metasource node"
            
                count = await core.count('inet:server')
                assert count == 4, "Count of inet:server nodes should be 4"

                count = await core.count('inet:http:request')
                assert count == 165, "Count of inet:http:request nodes should be 165"

                count = await core.count('inet:dns:a')
                assert count == 7, "Count of inet:dns:a nodes should be 7"

                count = await core.count('inet:whois:rec')
                assert count == 9, "Count of inet:whois:rec nodes should be 9"

