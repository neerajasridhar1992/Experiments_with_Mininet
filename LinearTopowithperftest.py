#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class LinearTopo(Topo):
   "Linear topology of k switches, with one host per switch."

   def __init__(self, k=2, **opts):
       """Init.
           k: number of switches (and hosts)
           hconf: host configuration options
           lconf: link configuration options"""

       super(LinearTopo, self).__init__(**opts)

       self.k = k

       lastSwitch = None
       for i in irange(1, k):
           host = self.addHost('h%s' % i)
           switch = self.addSwitch('s%s' % i)
           self.addLink( host, switch)
           if lastSwitch:
               self.addLink( switch, lastSwitch)
           lastSwitch = switch

def perfTest():
   "Create and test a simple network"
   topo = LinearTopo(k=4)
   net = Mininet(topo)
   net.start()
   print "Dumping host connections"
   dumpNodeConnections(net.hosts)
   print "Testing network connectivity"
   net.pingAll()
   
   print "Testing bandwidth between h1 and h2"
   h1, h2 = net.get('h1', 'h2')
   net.iperf((h1, h2))
   
   print "Testing bandwidth between h1 and h3"
   h1, h3 = net.get('h1', 'h3')
   net.iperf((h1, h3))
   
   print "Testing bandwidth between h1 and h4"
   h1, h4 = net.get('h1', 'h4')
   net.iperf((h1, h4))
   
   print "Testing bandwidth between h2 and h3"
   h2, h3 = net.get('h2', 'h3')
   net.iperf((h2, h3))
   
  
   print "Testing bandwidth between h2 and h4"
   h2, h4 = net.get('h2', 'h4')
   net.iperf((h2, h4))
   
   print "Testing bandwidth between h3 and h4"
   h3, h4 = net.get('h3', 'h4')
   net.iperf((h3, h4))
   net.stop()

if __name__ == '__main__':
   # Tell mininet to print useful information
   setLogLevel('info')
   perfTest()
