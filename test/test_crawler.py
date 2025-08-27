import re
import synapse.tests.utils as s_t_utils
from synapse.tools import genpkg
from aioresponses import aioresponses

from .common import get_mock_file_content, BASE_URL, SYNAPSE_PACKAGE_YAML

class TestCrawler(s_t_utils.SynTest):

    @aioresponses()
    async def test_fqdn_http(self, mocked: aioresponses):
        mocked.get(
            re.compile(f'^{re.escape(BASE_URL + 'axon/domain/crawl/history/'+'www.validin.com')}'),
            status=200,
            body=get_mock_file_content('axon_domain_crawl_history_www.validin.com.json')
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            with self.getAsyncLoggerStream('synapse.storm.log') as stream:
                # Run the storm command to trigger the crawl
                await core.callStorm('[inet:fqdn=www.validin.com] | s1.validin.http')

                metasource_iden = await core.callStorm('meta:source:name="validin api" | return($node.repr())')
                assert metasource_iden, "Find metasource node"
            
                count = await core.count('inet:server')
                assert count == 2, "Count of inet:server nodes should be 2"

                count = await core.count('inet:http:request')
                assert count == 9, "Count of inet:http:request nodes should be 9"

    @aioresponses()
    async def test_ip_http(self, mocked: aioresponses):
        mocked.get(
            re.compile(f'^{BASE_URL + 'axon/ip/crawl/history/'+'138.197.40.194'}'),
            status=200,
            body=get_mock_file_content('axon_ip_crawl_history_138.197.40.194.json')
        )

        pkgdef = genpkg.loadPkgProto(SYNAPSE_PACKAGE_YAML)
        async with self.getTestCore() as core:
            await core.addStormPkg(pkgdef)
            with self.getAsyncLoggerStream('synapse.storm.log') as stream:
                # Run the storm command to trigger the crawl
                await core.callStorm('[inet:ipv4=138.197.40.194] | s1.validin.http')

                metasource_iden = await core.callStorm('meta:source:name="validin api" | return($node.repr())')
                assert metasource_iden, "Find metasource node"
            
                count = await core.count('inet:server')
                assert count == 1, "Count of inet:server nodes should be 1"
                
                count = await core.count('inet:http:request')
                assert count == 10, "Count of inet:http:request nodes should be 10"
