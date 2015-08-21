'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ['HOME']

''' Add your global variables here ... '''


class Firewall(EventMixin):

    mac_pair = set()

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")
        self.parse_policy()
        log.debug("Parse Policy")

    def parse_policy(self):
        f = open(policyFile, 'r')
        lines = f.read().splitlines()

        for line in lines[1:]:  # skip the first line
            policy = line.split(',')
            self.mac_pair.add((policy[1], policy[2]))
        #print self.mac_pair

    def _handle_ConnectionUp(self, event):
        ''' Add your logic here ... '''
        for tu in self.mac_pair:
            msg = of.ofp_flow_mod()
            msg.priority = 12345
            # no actions
            #msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
            msg.actions = []
            msg.match.dl_src = EthAddr(tu[0])
            msg.match.dl_dst = EthAddr(tu[1])
            #msg.buffer_id = None
            event.connection.send(msg)
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))


def launch():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
