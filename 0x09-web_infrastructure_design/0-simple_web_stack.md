# Simple Web Stack
## explain some specifics
+ What a server is.<br/>A server is a computer hardware or software that provides services to other computers, which are usually referred to as *clients*.

+ What is the role of the domain name.<br/>Domain names serve to identify Internet resources, such as computers, networks, and services, with a text-based label that is easier to memorize than the numerical addresses used in the Internet protocols. A domain name may represent entire collections of such resources or individual instances.

+ The type of DNS record `www` is in `www.foobar.com`.<br/>`www.foobar.com` uses an **A record**. This can be checked by running `dig www.foobar.com`.<br/>**Note:** the results might be different but for the infrastructure in this design, an **A** record is used.<br/>
<i>Address Mapping record (A Record)—also known as a DNS host record, stores a hostname and its corresponding IPv4 address.</i>

+ The role of the web server.<br/>The web server is a software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.

+ The role of the application server.<br/>To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

+ The role of the database.<br/>To maintain a collection of organized information that can easily be accessed, managed and updated

+ What the server uses to communicate with the client (computer of the user requesting the website).<br/>Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

## Issues With This Infrastructure
+ There are multiple SPOF (Single Point Of Failure) in this infrastructure.<br/>For example, if the MySQL database server is down, the entire site would be down.

+ Downtime when maintenance needed.<br/>When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off.

+ Cannot scale if there's too much incoming traffic.<br/>The server can quickly run out of resources or slow down when it starts receiving a lot of requests.
