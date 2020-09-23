## Planning Service

<table>
<thead>
<tr class="header">
<th><strong>Technical Description</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Security Mechanisms</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name</td>
<td>Description</td>
<td>Type</td>
</tr>
<tr class="odd">
<td>TLS 1.2</td>
<td>The service relies on TLS 1.2 to provide integrity and confidentiality.</td>
<td><ul>
<li><p>AUTHENTICATION</p></li>
<li><p>CONFIDENTIALITY</p></li>
<li><p>INTEGRITY</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Cypher Suites</td>
<td><p>The following cipher suites are allowed in accordance with ECRYPT-CSA recommendations https://www.ecrypt.eu.org/csa/documents/D5.4-FinalAlgKeySizeProt.pdf:</p>
<ul>
<li><p>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</p></li>
<li><p>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</p></li>
</ul></td>
<td><ul>
<li><p>AUTHENTICATION</p></li>
<li><p>CONFIDENTIALITY</p></li>
<li><p>INTEGRITY</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>X.509v3 Server Certificate</td>
<td>The service utilizes X.509v3 public certificate to authenticate the provider.</td>
<td><ul>
<li><p>AUTHENTICATION</p></li>
</ul></td>
</tr>
<tr class="even">
<td>X.509v3 Client Certificate</td>
<td>The service utilizes X.509v3 public certificate to authenticate the consumer.</td>
<td><ul>
<li><p>AUTHENTICATION</p></li>
</ul></td>
</tr>
</tbody>
</table>

| **Behaviour**   |                                                                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**        | Planning Service with REJ or non-concur preliminary flight plan                                                                                                                                                                                         |
| **Description** | This example illustrates the submission of a new preliminary flight plan that is rejected by the eASP for any reason, be it technical (such as syntax error in the request) or operational (such as penetrating a closed airspace). See XXX for details |

| **Behaviour**   |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| **Name**        | Planning Service with CONCUR (operationally acceptable) preliminary file plan                                              |
| **Description** | This example illustrates the submission of a new preliminary flight plan that is accepted by the eASP. See XXX for details |

| **Behaviour**   |                                                                |
|-----------------|----------------------------------------------------------------|
| **Name**        | Planning Service with manually treated preliminary flight plan |
| **Description** | See Case c) Filing Service with manually treated flight plan.  |

| **Behaviour**   |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| **Name**        | Planning Service with Preliminary Flight Plan requiring negotiation                                                     |
| **Description** | This example illustrates the submission of a new preliminary flight plan that requires negotiation. See XXX for details |

| **Endpoints**            |                 |             |
|--------------------------|-----------------|-------------|
| **Name**                 | **Description** | **Address** |
| **operational endpoint** | TBD             | https…      |

| **Service Description References (Implemented Standard)** |                                                                                                                        |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Name**                                                  | ECTL SWIM TI YP                                                                                                        |
| **Description**                                           | This specification contains requirements for system interfaces (e.g. protocols) and for IT infrastructure capabilities |
| **Version**                                               | v1.0                                                                                                                   |
| **Reference**                                             | public://2019-11/EUROCONTROL-SPEC-170 SWIM TIYP Ed 1.0.pdf                                                             |
| **Standard Type**                                         | EUROCONTROL\_SPECIFICATION\_FOR\_SWIM\_TECHNICAL\_INFRASTRUCTURE                                                       |
| **Conformance Statement**                                 | Implementation of service and network bindings                                                                         |
| **Is conformant**                                         | true                                                                                                                   |

| **Service Description References (Service Document)** |                                      |
|-------------------------------------------------------|--------------------------------------|
| **Name**                                              | PlanningServiceExample.wsdl          |
| **Description**                                       | TBD                                  |
| **Version**                                           | TBD                                  |
| **Reference**                                         | TBD                                  |
| **Document Type**                                     | Machine readable service description |

| **Service Description References (Service Document)** |                                                       |
|-------------------------------------------------------|-------------------------------------------------------|
| **Name**                                              | FficeTemplates.xsd                                    |
| **Description**                                       | TBD                                                   |
| **Version**                                           | 1.0                                                   |
| **Reference**                                         | \\schemas\\applications\\fficemessage\\fficetemplates |
| **Document Type**                                     | Machine readable message description                  |

### Example WSDL

> For operation submitPreliminaryFlightPlan:

<table>
<tbody>
<tr class="odd">
<td><p>&lt;definitions name="PlanningService"</p>
<p>xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"</p>
<p>xmlns="http://schemas.xmlsoap.org/wsdl/"</p>
<p>&gt;</p>
<p>&lt;!-- omitted types section with content model schema info --&gt;</p>
<p>&lt;message name="preliminaryFlightPlanSubmissionReply"&gt;</p>
<p>&lt;part name="body" element="preliminaryFlightPlanSubmissionReply"/&gt;</p>
<p>&lt;/message&gt;</p>
<p>&lt;message name="preliminaryFlightPlanSubmissionRequest"&gt;</p>
<p>&lt;part name="body" element="preliminaryFlightPlanSubmissionRequest"/&gt;</p>
<p>&lt;/message&gt;</p>
<p>&lt;portType name="PreliminaryFlightPlanSubmissionRequestPortType"&gt;</p>
<p>&lt;operation name="submitPreliminaryFlightPlan"&gt;</p>
<p>&lt;input message="preliminaryFlightPlanSubmissionRequest"/&gt;</p>
<p>&lt;output message="preliminaryFlightPlanSubmissionReply"/&gt;</p>
<p>&lt;/operation&gt;</p>
<p>&lt;/portType&gt;</p>
<p>&lt;binding name="PlanningProvider-eASPBinding"</p>
<p>type="PreliminaryFlightPlanSubmissionRequestPortType"&gt;</p>
<p>&lt;soap:binding style="document"</p>
<p>transport="http://schemas.xmlsoap.org/soap/http"/&gt;</p>
<p>&lt;operation name="preliminaryFlightPlanSubmissionRequest"&gt;</p>
<p>&lt;soap:operation</p>
<p>soapAction="http://www.example-FIXM-FFICE.aero/PlanningService"/&gt;</p>
<p>&lt;input&gt;</p>
<p>&lt;soap:body use="literal"</p>
<p>namespace="http://www.example-FIXM-FFICE.aero/PlanningService.xsd"/&gt;</p>
<p>&lt;/input&gt;</p>
<p>&lt;output&gt;</p>
<p>&lt;soap:body use="literal"</p>
<p>namespace="http://www.example-FIXM-FFICE.aero/PlanningService.xsd"/&gt;</p>
<p>&lt;/output&gt;</p>
<p>&lt;fault&gt;</p>
<p>&lt;soap:body use="literal"</p>
<p>namespace="http://www.example-FIXM-FFICE.aero/PlanningService.xsd"/&gt;</p>
<p>&lt;/fault&gt;</p>
<p>&lt;/operation&gt;</p>
<p>&lt;/binding&gt;</p>
<p>&lt;service name="PlanningService"&gt;</p>
<p>&lt;port name="PlanningProvider-eASP"</p>
<p>binding="PlanningProvider-eASPBinding"&gt;</p>
<p>&lt;soap:address location="http://www.example-FIXM-FFICE.aero/PlanningService"/&gt;</p>
<p>&lt;/port&gt;</p>
<p>&lt;/service&gt;</p>
<p>&lt;/definitions&gt;</p></td>
</tr>
</tbody>
</table>

### Service Behaviour

To illustrate the planning service behavior and associated interactions,
four cases are distinguished:

-   The ***Preliminary Flight Plan Message*** submission is rejected
    (***REJ or NON CONCUR***). For details see \[10\] Page II-4-13
    Section 4.4.5.4 and \[10\] Page II-5-29 Section 5.3.7 iii

-   The ***Preliminary Flight Plan Message*** submission is accepted
    (***ACK & CONCUR***). For details see \[10\] Page II-4-13 Section
    4.4.5.2/4.4.5.3 and \[10\] Page II-5-28 Section 5.3.7 i

-   The ***Preliminary Flight Plan Message*** submission requires manual
    intervention (***MAN***). For details see \[10\] Page II-4-13
    Section 4.4.5.5

-   The ***Preliminary Flight Plan Message*** submission requires
    negotiation (**NEGOTIATE**) as described in \[10\] Page II-5-29
    Section 5.3.7 ii

Case a) Planning Service with REJ or non-concur preliminary flight plan

**Description  
**This example illustrates the submission of a new preliminary flight
plan that is rejected by the eASP for any reason, be it technical (such
as syntax error in the request) or operational (such as penetrating a
closed airspace).

**Expected FF-ICE interaction**

<img src=".//media/image235.png" style="width:4.05764in;height:3.18264in" alt="Picture1" />

<span id="_Toc498700597" class="anchor"></span>Figure 13: FF-ICE
interaction for REJ or non-concur flight plan submission

According to the FF-ICE/R1 Implementation Guidance Manual \[10\], the
submission could be:

1.  Rejected immediately for having failed data acceptability: in this
    case a ***Submission Response*** = ***REJ*** is used and no
    ***Planning Status Message*** is to follow.

2.  Accepted with respect to data acceptability but not accepted due to
    operational acceptability: if the data acceptability is performed at
    a later stage this should result in a ***Submission Response*** =
    ***ACK*** followed by a ***Planning Status*** ***Message*** with the
    errors.

**Example implementation**

<img src=".//media/image236.png" style="width:5.36493in;height:1.53284in" />

<span id="_Toc48644003" class="anchor"></span>Figure 14: Preliminary
Flight plan submission example with preliminary flight plan rejected for
having failed data acceptability (REJ)

-   The PreliminaryFlightPlanSubmissionRequest contains the flight plan
    encoded in FIXM 4.1.0.

-   The PreliminaryFlightPlanSubmissionReply contains the status
    ***REJ*** and the reason.

<img src=".//media/image237.png" style="width:5.46389in;height:1.69306in" />

<span id="_Toc48644004" class="anchor"></span>Figure 15: Preliminary
Flight plan submission example with preliminary flight plan rejected for
having failed operational acceptability (NON CONCUR)

-   The preliminaryFlightPlanSubmissionRequest contains the flight plan
    encoded in FIXM 4.1.0.

-   The preliminaryFlightPlanSubmissionReply contains the status
    ***ACK***.

-   The planningStatusMaessage contains the ***Planning Status*** with
    status ***NON CONCUR.***

Whatever the submission operation, the FF-ICE/R1 Implementation Guidance
Manual \[10\] always makes a distinction between data acceptability and
operational acceptability. However, some eASP may want to perform the
two together as part of the same transaction. This would translate into
the following figure.

<img src=".//media/image236.png" style="width:6.27083in;height:1.79167in" />

<span id="_Toc48644005" class="anchor"></span>Figure 16: Preliminary
Flight plan submission example with rejected (REJ or ACK+NON CONCUR)
preliminary flight plan

In this example, the data acceptability and operational acceptability
are combined into the same transaction. The resulting synchronous reply
conveys all necessary information: the ***REJ*** status and the
operational reason that led to the ***NON CONCUR***. As outlined by the
diagram, the interaction only takes place as a R/R and does not need to
generate any asynchronous messages.

-   The PreliminaryFlightPlanSubmissionRequest contains the flight plan
    encoded in FIXM 4.1.0.

-   The PreliminaryFlightPlanSubmissionReply contains the status
    ***REJ*** and the reason or ***ACK*** and ***NON CONCUR***. In
    FF-ICE/R1 terminology this reply implements both the ***Submission
    Response*** and the ***Planning Status***.

Case b) Planning Service with CONCUR (operationally acceptable)
preliminary file plan

**Description**  
This example illustrates the submission of a new preliminary flight plan
that is accepted by the eASP.

**Expected FF-ICE interaction**

<img src=".//media/image238.png" style="width:4.075in;height:1.56667in" />

<span id="_Toc48644006" class="anchor"></span>Figure 17: FF-ICE
interaction with accepted (CONCUR) preliminary flight plan

**Example implementation**

<img src=".//media/image237.png" style="width:5.46389in;height:1.69306in" />

<span id="_Ref508197419" class="anchor"></span>Figure 18: Preliminary
Flight plan submission example with accepted (CONCUR) preliminary flight
plan

-   The preliminaryFlightPlanSubmissionRequest contains the flight plan
    encoded in FIXM 4.1.0.

-   The preliminaryFlightPlanSubmissionReply contains the status
    ***ACK***.

-   The planningStatusMaessage contains the ***Planning Status*** with
    status ***CONCUR.***

Figure 18 mirrors the distinction between data acceptability and
operational acceptability that is introduced by the FF-ICE/R1
Implementation Guidance. However, both aspects may be addressed
technically as part of the same transaction, as illustrated by Figure
19.

<img src=".//media/image236.png" style="width:6.26806in;height:1.79087in" />

<span id="_Ref508197611" class="anchor"></span>Figure 19: Preliminary
Flight plan submission example with accepted (ACK and CONCUR)
preliminary flight plan

In this example, the data acceptability and operational acceptability
are combined into the same transaction. The request is processed
successfully and the preliminary flight plan is ***CONCUR***
(operationally acceptable).

-   The preliminaryFlightPlanSubmissionRequest contains the preliminary
    flight plan encoded in FIXM 4.1.0.

-   The preliminaryFlightPlanSubmissionReply contains the status
    ***ACK*** and the accepted preliminary flight plan encoded in FIXM
    4.1.0. In FF-ICE terminology this reply contains both the
    ***Submission Response*** and the ***Planning Status***.

Case c) Planning Service with manually treated preliminary flight plan

See Case c) Filing Service with manually treated flight plan.

Case d) Planning Service with Preliminary Flight Plan requiring
negotiation

**Description**  
This example illustrates the submission of a new preliminary flight plan
that requires negotiation.

**Expected FF-ICE interaction**

<img src=".//media/image239.png" style="width:4.075in;height:1.56042in" />

<span id="_Toc48644009" class="anchor"></span>Figure 20: FF-ICE
interaction with preliminary flight plan that requires negotiation
(NEGOTIATE)

**Example implementation**

<img src=".//media/image237.png" style="width:5.46389in;height:1.69306in" />

<span id="_Ref508264559" class="anchor"></span>Figure 21: Preliminary
Flight plan submission example with preliminary flight plan that
requires negotiation (NEGOTIATE)

-   The preliminaryFlightPlanSubmissionRequest contains the flight plan
    encoded in FIXM 4.1.0.

-   The preliminaryFlightPlanSubmissionReply contains the status
    ***ACK***.

-   The planningStatusMaessage contains the ***Planning Status*** with
    status ***NEGOTIATE.***

Figure 21 mirrors the distinction between data acceptability and
operational acceptability that is introduced by the FF-ICE/R1
Implementation Guidance. However, both aspects may be addressed
technically as part of the same transaction:

<img src=".//media/image236.png" style="width:6.26806in;height:1.79087in" />

<span id="_Toc48644011" class="anchor"></span>Figure 22: Preliminary
Flight plan submission example with preliminary flight plan that
requires negotiation (ACK and NEGOTIATE)

In this example, the data acceptability and operational acceptability
are again combined into the same transaction. The request is processed
successfully and the preliminary flight plan is ***NEGOTIATE***
(requires negotiation).

-   The preliminaryFlightPlanSubmissionRequest contains the preliminary
    flight plan encoded in FIXM 4.1.0.

-   The preliminaryFlightPlanSubmissionReply contains the status
    ***ACK*** and the proposed for negotiation preliminary flight plan
    encoded in FIXM 4.1.0. In FF-ICE terminology this reply contains
    both the ***Submission Response*** and the ***Planning Status***.

#### Data Implementation Description

This part will be addressed in a future version of the document.

