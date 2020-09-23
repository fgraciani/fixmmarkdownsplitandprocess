## Applicable FIXM version

The present version of the document supports the implementation of the
following FIXM components:

-   **FIXM Core v4.2.0** \[1\]

-   **FIXM Applications**

    -   **FF-ICE Message v1.0.0**

    -   **Basic Message v1.0.0**

**What is new in FIXM Core 4.2.0?**

At high level, the scope declaration of FIXM Core 4.2.0 is the same as
FIXM 4.1.0, namely to provide harmonised representation of the flight
data structures exchanged in the context of FF-ICE/R1. FIXM Core 4.2.0,
however, implements significant improvements compared to FIXM 4.1.0:

-   FIXM Core 4.2.0 is based on the draft FF-ICE/R1 Implementation
    Guidance Manual version 0.91, therefore reflecting a more mature -
    but yet not final - version of the FF-ICE/R1 requirements specified
    by the ICAO ATMRPP;

-   FIXM Core 4.2.0 contains more usable data structures for enabling a
    better representation of the feedback that an eAU can get from an
    eASP after submitting an FF-ICE flight plan;

-   FIXM Core 4.2.0 supports nillable properties (which FIXM 4.1.0 did
    not)[1] that enable proper FF-ICE Flight Plan updates as described
    in the FF-ICE/R1 Implementation Guidance Manual;

-   FIXM Core 4.2.0 comes together with a new FF-ICE Application Library
    that addresses the use of FIXM Core in the specific context of
    FF-ICE and which provides formal representation of the individual
    FF-ICE messages. A new “Basic Message” library is also available in
    order to provide basic messaging support for FIXM.

-   FIXM Core 4.2.0 also implements a number of technical improvements
    and bug corrections.

Important note: This document does not detail the individual changes
implemented in this new FIXM release. More information about these
changes can be found in the FIXM Release Note and in the online
repository of FIXM Change Requests from the FIXM Work Area. This
document rather focuses on how to use the various FIXM components and
data structures.

