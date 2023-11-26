# Distributed Web Infrastructure
## Specifics About This Infrastructure
+ The distribution algorithm the load balancer is configured with and how it works.<br/>Referencing the load-balancer pool in its configuration file, HAProxy determines the application server to route the client request to, based on a round-robin system. This server receiving the request is generally part of an auto-scaling array consisting of dedicated application servers.
+ Is the load-balancer enabling an Active-Active or Active-Passive setup.<br/>HAProxy, as a load balancer, can be configured to operate in both Active-Active and Active-Passive setups. In an **Active-Active** setup, all nodes or servers in the load balancing pool are actively serving traffic simultaneously.But in an **Active-Passive** setup, only one node or server actively serves traffic at any given time, while the others remain on standby.
+ How a database Primary-Replica (Master-Slave) cluster works <br/>Master-Slave cluster is a configuration in which there is one primary/master database and one or more replica/slave databases. This setup is commonly used to achieve goals such as high availability, fault tolerance, and scalability.
+ The difference between the *Primary* node and the *Replica* node in regard to the application.<br/>The *Primary* node is responsible for all the write operations the site needs whilst the *Replica* node is capable of processing read operations, which decreases the read traffic to the *Primary* node.

## Issues With This Infrastructure

+ Where are SPOF <br/>if the Primary MySQL database server is down, the entire site would be unable to make changes to the site.
+ Security issues (no firewall, no HTTPS)<br/>The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
+ No monitoring.<br/>We have no way of knowing the status of each server since they're not being monitored.
