# Secured and monitored web infrastructure
## Specifics About This Infrastructure

+ The purpose of the firewalls.<br/>The firewalls are for protecting the network (web servers, anyway) from unwanted and unauthorized users.
+ The purpose of the SSL certificate.<br/> The SSL certificate is for encrypting the traffic between the web servers and the external network.
+ The purpose of the monitoring clients. <br/> The monitoring clients are for monitoring the servers and the external network.

##Issues With This Infrastructure

+ Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted.
+ Having one MySQL server is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.
+ Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc.
