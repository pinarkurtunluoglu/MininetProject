# Mininet Project

First of all, I installed two separate virtual machines for my project. I installed one Mininet and the other Ubuntu 22.04. I downloaded OpenDayLight from the Ubuntu machine and tried to create a simple topology over Mininet and see it with OpenDayLight.  

I embedded the OpenFlow rules into the switches in the topology I created with Mininet with below codes.

#mininet> s1 ovs-ofctl add-flow s1 "priority=1, actions=output:2"
#mininet> s2 ovs-ofctl add-flow s2 "priority=1, actions=output:3"
#mininet> s3 ovs-ofctl add-flow s3 "priority=1, actions=output:2"

In the continuation of the project, I wrote a code that allows finding the shortest path in a network topology using the OpenDaylight controller. Also, I found the densest switchs in the OpenFlow switchs based on packet statistics and made Decalculation of the shortest path between these switchs.

