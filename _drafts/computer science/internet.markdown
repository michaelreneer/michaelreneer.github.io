status: draft
Title: Internet
Date: 2013-7-14
Tags: computer science, internet
Subtitle: 

[&#x21d0; Table Of Contents][]

## How Browsers Work {: #how_browsers_work }

- http://www.html5rocks.com/en/tutorials/internals/howbrowserswork/

<!-- TODO: content -->

## DNS {: #dns }

- Domain Name System is a hierarchical distributed naming system for resources connected to a network.
- Translates domain names to IP addresses
- DNS Lookup
    - Browser asks **Recursive Name Server** where is www.michaelreneer.com?
    - It doesn't know but it:
        - Queries the **Internet Root Servers** to get the **TLD Name Servers** for the `.com` top level domain (TLD).
        - Queries the `.com` **TLD Name Servers** to get the **Authoritative Name Servers** for `michaelreneer.com`.
        - Queries the **Authoritative Name Servers** for `michaelreneer.com` to get the IP address for the host `www.michaelreneer.com` and return that IP address to your computer.

<!-- TODO: content -->

## TCP/IP {: #tcp_ip }

- A set of communications protocols used for the Internet and other networks.

<!-- TODO: content -->

#### Link Layer {: #link_layer }

- The link layer contains communication technologies for a single network segment (link) of a local area network.
- This layer defines the networking methods within the scope of the local network link on which hosts communicate without intervening routers. This layer describes the protocols used to describe the local network topology and the interfaces needed to effect transmission of Internet layer datagrams to next-neighbor hosts.

<!-- TODO: content -->

#### Internet Layer {: #internet_layer }

- The internet layer (IP) connects independent networks, thus establishing internetworking.
- The internet layer has the task of exchanging datagrams across network boundaries. It is therefore also referred to as the layer that establishes internetworking, indeed, it defines and establishes the Internet. This layer defines the addressing and routing structures used for the TCP/IP protocol suite. The primary protocol in this scope is the Internet Protocol, which defines IP addresses. Its function in routing is to transport datagrams to the next IP router that has the connectivity to a network closer to the final data destination.

<!-- TODO: content -->

#### Transport Layer {: #transport_layer }

- The transport layer handles host-to-host communication.
- The transport layer constitutes the networking regime between two network hosts, either on the local network or on remote networks separated by routers. The transport layer provides a uniform networking interface that hides the actual topology (layout) of the underlying network connections. This is where flow-control, error-correction, and connection protocols exist, such as TCP. This layer deals with opening and maintaining connections between Internet hosts.

<!-- TODO: content -->

#### Application Layer {: #application_layer }

- The application layer contains all protocols for specific data communications services on a process-to-process level. For example, the Hypertext Transfer Protocol (HTTP) specifies the web browser communication with a web server.
- This is the scope within which applications create user data and communicate this data to other processes or applications on another or the same host. The communications partners are often called peers. This is where the higher level protocols such as SMTP, FTP, SSH, HTTP, etc. operate.

<!-- TODO: content -->

## HTTP {: #http }

- GET, POST, PUT, DELETE, etc ...
- Clients and servers, clients initiate requests to servers; servers process requests and return appropriate responses.
- Polling.
- Server may not know who the client is or what they have already recieved, therefor duplicate data may be sent.

<!-- TODO: content -->

## REST {: #rest }

- REpresentational State Transfer
- A style of software architecture for distributed systems such as the World Wide Web.
- Typically uses normal HTTP methods instead of a big XML format describing everything. For example to obtain a resource you use HTTP GET, to put a resource on the server you use HTTP PUT. To delete a resource on the server you use HTTP DELETE.

<!-- TODO: content -->

## SOAP {: #soap }

- Simple Object Access Protocol
- SOAP is a method of transferring messages, or small amounts of information, over the Internet. SOAP messages are formatted in XML and are typically sent using HTTP (hypertext transfer protocol).
- SOAP builds an XML protocol on top of HTTP.
- SOAP describes functions, and types of data.

<!-- TODO: content -->

## RESTful API {: #restful_api }

- Web API implemented using HTTP and REST principles.
- Easier to cache responses then with SOAP.

<!-- TODO: content -->

## Websockets {: #websockets }

- Bi-directional communication.
- Standard part of HTML5.

<!-- TODO: content -->

[&#x21d0; Table Of Contents][]

[&#x21d0; table of contents]: ../study-guide/#basic_c_data_types "Table Of Contents"

