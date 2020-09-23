## The FF-ICE Application Library for FIXM

The FF-ICE Application Library is an Application Library[7] for FIXM
that addresses the specific use of FIXM Core in the context of ICAO
FF-ICE. It provides harmonized FF-ICE Message data structures and the
individual FF-ICE Message templates in line with the requirements on
FF-ICE Messages defined by the ICAO FF-ICE Implementation Guidance
Manual (ICAO Doc 9965 Volume II).

The content of the FF-ICE Application Library is the following:

> <img src=".//media/image27.png" style="width:3.28125in;height:4.80911in" />
> <img src=".//media/image28.png" style="width:2.55556in;height:2.4821in" />

<span id="_Toc48643984" class="anchor"></span>Figure 7: Overview of the
FF-ICE Message Application Library content

The FF-ICE Message Application Library is developed and published by the
FIXM CCB, together with FIXM Core.

*  
*

### FF-ICE Message data structures

The FF-ICE message data structures are the data elements that
specifically qualify the FF-ICE Messages. They do not describe a Flight
but are necessary for understanding the purpose and meaning of an FF-ICE
information exchange. The FF-ICE message data modelled by the FF-ICE
Application Library include:

-   A model element representing generically an FF-ICE Message with its
    identifier, timestamp, type etc. An enumeration provides the
    possible types of FF-ICE Messages: Filed Flight Plan message,
    Submission Response message, Filing Status message etc.

-   Model elements representing the different FF-ICE statuses with their
    possible values: Planning statuses CONCUR / NON\_CONCUR / NEGOTIATE,
    Filing statuses ACCEPTABLE / NOT\_ACCEPTABLE, Submission statuses
    ACK / MANUAL / REJECT etc.

-   Model elements representing the FF-ICE participants and their
    properties, which are used for identifying the operational
    stakeholders sending and receiving FF-ICE messages, or the list of
    relevant ASPs etc.

The FF-ICE Message data structures are traceable to the FF-ICE
Implementation Guidance Manual Appendix B. For instance:

<img src=".//media/image29.png" style="width:6.28125in;height:2.09225in" />

<span id="_Toc48643985" class="anchor"></span>Figure 8: Example of
FF-ICE Message data structures tracing to the FF-ICE Implementation
Guidance Manual, Appendix B

The FF-ICE message data structures other than Choices and Codelists are
extendable. This enables implementers to accommodate additional FF-ICE
message data structures required locally or regionally, in support of
local or regional FF-ICE requirements. Extension hooks are defined in a
similar fashion as for FIXM Core data structures.

The picture below provides an overview of the FF-ICE Message data
structures modelled in the FF-ICE Application Library.

<img src=".//media/image30.png" style="width:7.53603in;height:5.592in" />

<span id="_Toc48643986" class="anchor"></span>Figure 9: Overview of the
FF-ICE Message Data Structures

