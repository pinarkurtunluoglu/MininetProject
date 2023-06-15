# Mininet Project

First of all, I installed two separate virtual machines for my project. I installed one Mininet and the other Ubuntu 22.04. I downloaded OpenDaylight from the Ubuntu machine and tried to create a simple topology over Mininet and see it with OpenDaylight.  

![Screenshot from 2023-06-15 21-59-58](https://github.com/pinarkurtunluoglu/MininetProject/assets/77545059/038eefd1-9544-4764-b8fe-728353a4c589)

![Uploading Ekran Alıntısıı.png…]()

I embedded the OpenFlow rules into the switches in the topology I created with Mininet with below codes.

mininet> s1 ovs-ofctl add-flow s1 "priority=1, actions=output:2"
mininet> s2 ovs-ofctl add-flow s2 "priority=1, actions=output:3"
mininet> s3 ovs-ofctl add-flow s3 "priority=1, actions=output:2"



