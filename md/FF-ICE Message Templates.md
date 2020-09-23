## FF-ICE Message Templates

### Overview 

The FF-ICE Message templates are the representations of the individual
FF-ICE messages that are exchanged by the FF-ICE Services. Thirteen
message templates are defined in the FF-ICE Application library v1.0.0.
They correspond to the thirteen FF-ICE Messages described in the
FF-ICE/R1 Implementation Guidance Manual, Appendix C. The following
table provides the correspondence between the FF-ICE message templates
from the library and their corresponding description in the FF-ICE
Implementation Guidance Manual, Appendix C.

<span id="_Toc48644024" class="anchor"></span>Table 1: Correspondences
between FF-ICE Message templates and their ICAO Doc 9965 Volume II
description

| **FF-ICE Message templates** | **Associated Requirements from the FF-ICE Implementation Guidance Manual, Appendix C** |
|------------------------------|----------------------------------------------------------------------------------------|
| FiledFlightPlan              | C-4 Filed Flight Plan                                                                  |
| FilingStatus                 | C-5 Filing Status                                                                      |
| FlightArrival                | C-13 Flight Arrival                                                                    |
| FlightCancellation           | C-8 Flight Cancellation                                                                |
| FlightDataRequest            | C-10 Flight Data Request                                                               |
| FlightDataResponse           | C-11 Flight Data Response                                                              |
| FlightDeparture              | C-12 Flight Departure                                                                  |
| FlightPlanUpdate             | C-9 Flight Plan Update                                                                 |
| PlanningStatus               | C-3 Planning Status                                                                    |
| PreliminaryFlightPlan        | C-2 Preliminary Flight Plan                                                            |
| SubmissionResponse           | C-1 Submission Response                                                                |
| TrialRequest                 | C-6 Trial Request                                                                      |
| TrialResponse                | C-7 Trial Response                                                                     |

The FF-ICE Message templates define concretely the restricted subsets of
the FF-ICE Message data elements of the FIXM Core flight elements that
are relevant for each FF-ICE message transaction. They explicitly
declare which elements are mandatory, optional or irrelevant in each
case, and enforce stricter content patterns as appropriate.

### Example of the FF-ICE ‘Flight Cancellation’ Message

The following table is a simplified version of table C-8 from the FF-ICE
Implementation Guidance Manual, Appendix C. It describes the content of
the FF-ICE Flight Cancellation Message and indicates which fields are
mandatory (highlighted **in bold** in this document) or optional
(highlighted in *in italic*).

<span id="_Toc48644025" class="anchor"></span>Table 2: Example of the
FF-ICE Flight Cancellation Message

| **Data Category**          | **Data Item**                            | **Requirement** |
|----------------------------|------------------------------------------|-----------------|
| Message Information        | **List of Recipients**                   | **Mandatory**   |
|                            | **Message Originator**                   | **Mandatory**   |
|                            | *Request for Translation and Forwarding* | *Optional*      |
|                            | *Requested Recipients*                   | *Optional*      |
|                            | **Message Date-Time**                    | **Mandatory**   |
|                            | **Message Identifier**                   | **Mandatory**   |
|                            | **Type of Request/Response**             | **Mandatory**   |
|                            | *AFTN Address*                           | *Optional*      |
|                            | *Contact Information*                    | *Optional*      |
| Flight Identification      | **GUFI**                                 | **Mandatory**   |
|                            | **GUFI Originator**                      | **Mandatory**   |
|                            | **Aircraft Identification**              | **Mandatory**   |
| Departure/Destination Data | **Departure Aerodrome**                  | **Mandatory**   |
|                            | **Destination Aerodrome**                | **Mandatory**   |
|                            | **Estimated Off-Block Time**             | **Mandatory**   |

The FF-ICE Application library translates this table into an
implementable message template. This is illustrated by the picture
below. The message template resulting from the translation of this table
is displayed with a blue background.

<img src=".//media/image31.png" style="width:6.744in;height:8.38352in" />

<span id="_Toc48643987" class="anchor"></span>Figure 10: The FF-ICE
Flight Cancellation Message Template

<img src=".//media/image32.png" style="width:3.21736in;height:3.35069in" />**Explanations**

**XSD complex type restrictions** are used to pare down the Flight and
the FF-ICE Message data structures to just those fields that are
applicable to the Flight Cancellation Message, as well as to enforce
stricter optionality and content patterns where appropriate.

The XSD complex type restrictions are implemented by creating a new
class that generalizes the class to be restricted and then applying the
&lt;&lt;XSDrestriction&gt;&gt; stereotype to the generalization
connector, as shown in brown on the picture opposite.

<img src=".//media/image33.png" style="width:3.70486in;height:2.49722in" />

XML elements being irrelevant in the context of the message template are
eliminated by removing them from the model, as shown in red on the
picture opposite. Elements being mandatory in the context of the message
template have their cardinality set to (at least) 1 in the restriction,
as shown in blue.

<img src=".//media/image34.png" style="width:1.82708in;height:1.06042in" />In
general, all optionality, cardinality, and pattern restrictions are
implemented by applying the desired changes to the restricted class.

Because XSD complex type restrictions must use the same namespace as the
types they restrict, it is necessary to change their names. The
convention used in the FF-ICE Application Library is to prepend each
restricted class with “Ffice” plus an initialism of the message being
modeled – hence **FficeFC** for the FF-ICE **<u>F</u>**light
**<u>C</u>**ancellation Message.

Restricted classes require the restricted versions of associated
sub-classes. XSD complex type restrictions are therefore linked together
to form an entire restricted message. This provides clear guidance on
how the FF-ICE message template is constructed.

<img src=".//media/image35.png" style="width:7.47826in;height:3.78603in" />

