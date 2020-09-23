## FF-ICE/R1 Services Description Example

The purpose of this chapter is to provide informative examples of
service descriptions to realize the FF-ICE/R1 services[8] exchanging
FIXM flight plans.

### Role of FIXM in support of FF-ICE

As described in section XXX FIXM 4.2.0 introduces the FF-ICE Application
Library, a new component including a series of XML Schema templates that
support the encoding of the messages identified by FF-ICE/R1. While
these structures are an essential building block for realizing the
FF-ICE information exchanges, fully materializing the FF-ICE information
exchanges requires further descriptions of FF-ICE/R1 Services that
exchange FIXM-based FF-ICE/R1 messages.

FF-ICE/R1 Service implementation considerations are strictly speaking
beyond the scope of FIXM. This chapter only provides an <u>example</u>
of service description of FF-ICE/R1 Service implementations in order to
illustrate how FIXM can be used in support of FF-ICE and to help
implementers develop solutions for FF-ICE.

Describing a service implementation implies making a series of decisions
such as technology selection or naming strategies for service
operations. This chapter has no ambition to impose a particular
selection of technologies or particular service implementation
practices. It provides practical examples for illustration purpose only.

### Target audience

This chapter primarily targets an audience with knowledge of FF-ICE who
are interested in understanding how the information exchanges described
in the FF-ICE Implementation Guidance \[10\] can be realized using FIXM
and a selection of SOA technologies (e.g. AMQP, WSDL, SOAP). This
chapter also serves as a technical introduction to the information
exchanges described in the FF-ICE Implementation Guidance Manual, for
implementers not yet fully familiar with the FF-ICE concept.

This chapter assumes the reader is familiar with the FF-ICE/R1
principles, procedures and terminology outlined in the Manual on FF-ICE
Implementation Guidance \[10\].

### The FF-ICE/R1 Services

The FF-ICE/R1 Implementation Guidance \[10\] describes services as a set
of messages[9] that should be exchanged in the context of a described
behaviour (procedures).

The following diagram illustrates the services identified by FF-ICE/R1
and the associated messages.

A message is a discrete unit of communication intended by the source for
consumption by a given recipient or group of recipients. For example,
the ***Planning Service*** is described as a set of exchanges of
messages such as ***Preliminary Flight Plan Message*** or ***Planning
Status Message***.

### Technology Selection

In order to document the FIXM-Based examples in this section, two sets
of technologies have been selected that accommodate the need to exchange
the FF-ICE/R1 messages:

-   **SOAP Web Service technologies** allow to exchange request and
    reply messages where the initiative is taken by the service
    consumer.[10]

-   **AMQP** supports the exchange of notification messages where the
    initiative is taken by the service provider.

Appendix XXX Section YYY provides detailed rational for the technology
selection.

###  Planning Service Description Example

| **Service Name**                                                                                                                                                                  |                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Planning Service                                                                                                                                                                  |                                                                                                                                                       |
| **Abstract**                                                                                                                                                                      |                                                                                                                                                       |
| The Planning Service enables a CDM process between the eAU and the eASP(s) concerning the intended operation of a flight. It is described in \[10\], Page II-5-21 Section 5.1.    |                                                                                                                                                       |
| **Provision**                                                                                                                                                                     |                                                                                                                                                       |
| **Provider**                                                                                                                                                                      | Example Air Services (XAS)                                                                                                                            |
| **Provider Description**                                                                                                                                                          | XAS is a fictitious eASP used for illustration purposes.                                                                                              |
| **Provider Type**                                                                                                                                                                 | The Planning Service is an optional service expected or recommended to be provided by an eASP whose airspace is complex and/or regularly constrained. |
| **Categorisation**                                                                                                                                                                |                                                                                                                                                       |
| **Service Type**                                                                                                                                                                  | Swim compliant                                                                                                                                        |
| **Life Cycle Stage**                                                                                                                                                              | Operational                                                                                                                                           |
| **Business Activity Type**                                                                                                                                                        | Demand and capacity balancing                                                                                                                         |
| **Information Category**                                                                                                                                                          | Cooperative network information exchange                                                                                                              |
| **Intended Consumer**                                                                                                                                                             | The Planning Service is consumed by eAU(s).                                                                                                           |
| **Application Message Exchange Pattern**                                                                                                                                          | Request Reply                                                                                                                                         |
| **Operational Need**                                                                                                                                                              |                                                                                                                                                       |
| Assist the operator in determining the optimal route/trajectory for a flight by identifying the operational environment and ATM constraints applicable to the flight as proposed. |                                                                                                                                                       |
| Enable ATM service providers to obtain an earlier, more detailed and more accurate assessment of the anticipated traffic demand.                                                  |                                                                                                                                                       |
| **Functionality**                                                                                                                                                                 |                                                                                                                                                       |
| The ability to submit a preliminary flight plan and associated messages (Update, Cancel) and to provide the appropriate response messages (Submission Response, Planning Status)  |                                                                                                                                                       |

| **Service Interface**                     |                                  |
|-------------------------------------------|----------------------------------|
| **Name**                                  | Planning Provider eASP Interface |
| **Description**                           | TBD                              |
| **Interface provision side**              | Provider side interface          |
| **TI primitive message exchange pattern** | Synchronous request response     |
| **Service interface binding**             | SWIM\_TI\_YP\_1\_0\_WS\_SOAP     |
| **Network interface binding**             | TI\_YP\_1\_0.IPV4\_UNICAST       |

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>name</strong></td>
<td>submitPreliminaryFlightPlan</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>Request the submission of a new Preliminary Flight Plan</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Idempotency</strong></td>
<td>Idempotent</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Synchronicity</strong></td>
<td>Synchronous</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TI Protocol method</strong></td>
<td>HTTP POST</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td>preliminaryFlightPlanSubmissionRequest</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>Request of the submission of a new Preliminary Flight Plan.</p>
<p>Message template from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/preliminaryflightplan/fficemessage/FficePFP_FficeMessage.xsd"><strong>FficePFP_FficeMessage.xsd</strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Direction</strong></td>
<td>In</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="even">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>preliminaryFlightPlanSubmissionReply</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td><p>Reply returned in response to preliminaryFlightPlanSubmissionRequest</p>
<p>Message templates from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/submissionresponse/fficemessage/FficeSR_FficeMessage.xsd"><strong>FficeSR_FficeMessage.xsd</strong></a>, <a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/planningstatus/fficemessage/FficePS_FficeMessage.xsd"><strong>FficePS_FficeMessage.xsd</strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Direction</strong></td>
<td>Out</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="odd">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>name</strong></td>
<td>updatePreliminaryFlightPlan</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>Request the update of a Preliminary Flight Plan</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Idempotency</strong></td>
<td>Non idempotent</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Synchronicity</strong></td>
<td>Synchronous</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TI Protocol method</strong></td>
<td>HTTP POST</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td>preliminaryFlightPlanUpdateRequest</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>Request the update of a Preliminary Flight Plan</p>
<p>Message template from the FF-ICE Application:</p>
<p><strong><u>FficeFPU_FficeMessage.xsd</u></strong></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Direction</strong></td>
<td>In</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="even">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>preliminaryFlightPlanUpdateReply</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td><p>Reply returned in response to preliminaryFlightPlanUpdateRequest</p>
<p>Message templates from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/submissionresponse/fficemessage/FficeSR_FficeMessage.xsd"><strong>FficeSR_FficeMessage.xsd</strong></a>, <a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/planningstatus/fficemessage/FficePS_FficeMessage.xsd"><strong>FficePS_FficeMessage.xsd</strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Direction</strong></td>
<td>Out</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="odd">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>name</strong></td>
<td>cancelPreliminaryFlightPlan</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>Request the cancellation of a Preliminary Flight Plan</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Idempotency</strong></td>
<td>Non idempotent</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Synchronicity</strong></td>
<td>Synchronous</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TI Protocol method</strong></td>
<td>HTTP POST</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td>preliminaryFlightPlanCancellationRequest</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>Request the cancellation of a Preliminary Flight Plan</p>
<p>Message template from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/flightcancellation/fficemessage/FficeFC_FficeMessage.xsd"><strong><u>FficeFC_FficeMessage.xsd</u></strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Direction</strong></td>
<td>In</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="even">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>preliminaryFlightPlanCancellationReply</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td><p>Reply returned in response to preliminaryFlightPlanCancellationRequest</p>
<p>Message templates from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/submissionresponse/fficemessage/FficeSR_FficeMessage.xsd"><strong>FficeSR_FficeMessage.xsd</strong></a>, <a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/planningstatus/fficemessage/FficePS_FficeMessage.xsd"><strong>FficePS_FficeMessage.xsd</strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Direction</strong></td>
<td>Out</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="odd">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
</tbody>
</table>

Appendix XXX Section YYY provides detailed information regarding… TBD

### Filing Service Description Example

| **Service Name**                                                                                                                                                                                               |                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Filing Service                                                                                                                                                                                                 |                                                                                     |
| **Abstract**                                                                                                                                                                                                   |                                                                                     |
| The Filing Service enables the submission of filed flight plans (eFPL) in order to obtain air traffic services. It is described in \[10\], Page II-6-1 Section 6.                                              |                                                                                     |
| **Provision**                                                                                                                                                                                                  |                                                                                     |
| **Provider**                                                                                                                                                                                                   | Example Service Provider                                                            |
| **Provider Description**                                                                                                                                                                                       | The Example Service Provider is a non-existent eASP used for illustration purposes. |
| **Provider Type**                                                                                                                                                                                              | The Filing Service is provided by eASP(s).                                          |
| **Categorisation**                                                                                                                                                                                             |                                                                                     |
| **Service Type**                                                                                                                                                                                               | Swim compliant                                                                      |
| **Life Cycle Stage**                                                                                                                                                                                           | Operational                                                                         |
| **Business Activity Type**                                                                                                                                                                                     | Demand and capacity balancing                                                       |
| **Information Category**                                                                                                                                                                                       | Cooperative network information exchange                                            |
| **Intended Consumer**                                                                                                                                                                                          | The Filing Service is consumed by eAU(s).                                           |
| **Application Message Exchange Pattern**                                                                                                                                                                       | Request Reply                                                                       |
| **Operational Need**                                                                                                                                                                                           |                                                                                     |
| An eFPL should be filed in order to obtain air traffic services                                                                                                                                                |                                                                                     |
| **Functionality**                                                                                                                                                                                              |                                                                                     |
| The ability to submit a filed flight plan and associated messages (Update, Cancel) and to provide the appropriate response messages (Submission Response, Filing Status) in accordance with FF-ICE procedures. |                                                                                     |

| **Service Interface**                     |                                |
|-------------------------------------------|--------------------------------|
| **Name**                                  | Filing Provider eASP Interface |
| **Description**                           | TBD                            |
| **Interface provision side**              | Provider side interface        |
| **TI primitive message exchange pattern** | Synchronous request response   |
| **Service interface binding**             | SWIM\_TI\_YP\_1\_0\_WS\_SOAP   |
| **Network interface binding**             | TI\_YP\_1\_0.IPV4\_UNICAST     |

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>name</strong></td>
<td>submitFlightPlan</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>Request the submission of a new Flight Plan</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Idempotency</strong></td>
<td>Idempotent</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Synchronicity</strong></td>
<td>Synchronous</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TI Protocol method</strong></td>
<td>HTTP POST</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td>flightPlanSubmissionRequest</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>Request the submission of a new Flight Plan.</p>
<p>Message template from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/filedflightplan/fficemessage/FficeFFP_FficeMessage.xsd"><strong><u>FficeFFP_FficeMessage.xsd</u></strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Direction</strong></td>
<td>In</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="even">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>flightPlanSubmissionReply</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td><p>Reply returned in response to flightPlanSubmissionRequest</p>
<p>Message templates from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/submissionresponse/fficemessage/FficeSR_FficeMessage.xsd"><strong>FficeSR_FficeMessage.xsd</strong></a>, <a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/filingstatus/fficemessage/FficeFS_FficeMessage.xsd"><strong><u>FficeFS_FficeMessage.xsd</u></strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Direction</strong></td>
<td>Out</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="odd">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>name</strong></td>
<td>updateFlightPlan</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>Request the update of a Flight Plan</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Idempotency</strong></td>
<td>Non idempotent</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Synchronicity</strong></td>
<td>Synchronous</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TI Protocol method</strong></td>
<td>HTTP POST</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td>flightPlanUpdateRequest</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>Request the update of a Flight Plan</p>
<p>Message template from the FF-ICE Application:</p>
<p><strong><u>FficeFPU_FficeMessage.xsd</u></strong></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Direction</strong></td>
<td>In</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="even">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>flightPlanUpdateReply</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td><p>Reply returned in response to flightPlanUpdateRequest</p>
<p>Message templates from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/submissionresponse/fficemessage/FficeSR_FficeMessage.xsd"><strong>FficeSR_FficeMessage.xsd</strong></a>, <a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/filingstatus/fficemessage/FficeFS_FficeMessage.xsd"><strong><u>FficeFS_FficeMessage.xsd</u></strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Direction</strong></td>
<td>Out</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="odd">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>name</strong></td>
<td>cancelFlightPlan</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>Request the cancellation of a Flight Plan</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Idempotency</strong></td>
<td>Non idempotent</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Synchronicity</strong></td>
<td>Synchronous</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TI Protocol method</strong></td>
<td>HTTP POST</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td>flightPlanCancellationRequest</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>Request the cancellation of a Flight Plan</p>
<p>Message template from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/flightcancellation/fficemessage/FficeFC_FficeMessage.xsd"><strong><u>FficeFC_FficeMessage.xsd</u></strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Direction</strong></td>
<td>In</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="even">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Operation message</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td>flightPlanCancellationReply</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td><p>Reply returned in response to preliminaryFlightPlanCancellationRequest</p>
<p>Message templates from the FF-ICE Application:</p>
<p><a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/submissionresponse/fficemessage/FficeSR_FficeMessage.xsd"><strong>FficeSR_FficeMessage.xsd</strong></a>, <a href="https://www.fixm.aero/releases/FFICE-Msg-1.0.0/schemas/applications/fficemessage/fficetemplates/filingstatus/fficemessage/FficeFS_FficeMessage.xsd"><strong><u>FficeFS_FficeMessage.xsd</u></strong></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Direction</strong></td>
<td>Out</td>
<td><strong>Content Type</strong></td>
<td>text/xml</td>
</tr>
<tr class="odd">
<td><strong>Is fault</strong></td>
<td>False</td>
<td><strong>Content Encoding</strong></td>
<td></td>
</tr>
</tbody>
</table>

Appendix XXX Section YYY provides detailed information regarding… TBD

