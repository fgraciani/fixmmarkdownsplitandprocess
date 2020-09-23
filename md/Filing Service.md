## Filing Service

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

### Service Behaviour

To illustrate the filing service behaviour and associated interactions,
three cases are distinguished:

1.  The ***Filed Flight Plan*** is rejected (***REJ or NOT
    ACCEPTABLE***), as described in (resp.) \[10\] Page II-4-13 Section
    4.4.5.4 and Page II-6-2 Section 6.3.4 ii.

2.  The ***Filed Flight Plan*** is accepted (***ACK and ACCEPTABLE***),
    as described in (resp.) \[10\] Page II-4-13 Section
    4.4.5.2/4.4.5.3and Page II-6-1 Section 6.3.4 i

3.  The ***Filed Flight Plan*** requires manual intervention
    (***MAN***), as described in \[10\] Page II-4-13 Section 4.4.5.5

Case a) Filing Service with non-acceptable flight plan

**Description**  
This example illustrates the submission of a new flight plan that is
rejected by the eASP for any reason, be it technical (such as syntax
error in the request) or operational (such as penetrating a closed
airspace).

**  
**

**Expected FF-ICE interaction**

<img src=".//media/image240.png" style="width:4.08889in;height:1.57292in" />

<span id="_Toc48644012" class="anchor"></span>Figure 23: FF-ICE
interaction for invalid flight plan submission (REJ)

<img src=".//media/image241.png" style="width:4.08889in;height:1.57292in" />

<span id="_Toc498700589" class="anchor"></span>Figure 24: FF-ICE
interaction for non-acceptable flight plan submission

According to the FF-ICE conceptual document the submission could be:

1.  Rejected immediately for having failed data acceptability: in this
    case a ***Submission Response* = *REJ*** is used and no ***Filing
    Status Message*** is to follow.

2.  Accepted with respect to data acceptability but not accepted due to
    operational acceptability: if the data acceptability is performed at
    a later stage this should result in a ***Submission Response*** =
    ***ACK*** followed by a ***Filing Status*** with the errors.

**Example implementation**

<img src=".//media/image242.png" style="width:5.11458in;height:1.55764in" />

<span id="_Toc48644014" class="anchor"></span>Figure 25: Flight plan
filing submission example with filed flight plan rejected for having
failed data acceptability (REJ)

-   The flightPlanSubmissionRequest contains the flight plan encoded in
    FIXM 4.1.0

-   The flightPlanSubmissionReply contains the status ***REJ*** and the
    reason.

<img src=".//media/image243.png" style="width:5.08889in;height:1.52639in" />

<span id="_Toc48644015" class="anchor"></span>Figure 26: Flight plan
filing submission example with filed flight plan rejected for having
failed operational acceptability (NOT ACCEPTABLE)

-   The flightPlanSubmissionRequest contains the flight plan encoded in
    FIXM 4.1.0.

-   The flightPlanSubmissionReply contains the status ***ACK***.

-   The filingStatusMaessage contains the ***Filing Status*** with
    status ***NON ACCEPTABLE.***

As noted already for the Planning Service, both data acceptability and
operational acceptability may be addressed technically as part of the
same transaction.

<img src=".//media/image242.png" style="width:5.11458in;height:1.55764in" />

<span id="_Ref508205480" class="anchor"></span>Figure 27: Flight plan
filing submission example with rejected (REJ or ACT+NON ACCEPTABLE)
filed flight plan

By doing so, the synchronous reply conveys all necessary information:
the ***REJ*** status and the operational reason that led to the
***REJ***. As shown in Figure 27, the interaction only takes place as a
R/R and does not need to generate any asynchronous messages.

The flightPlanSubmissionReply contains the status ***REJ*** and the
reason. In FF-ICE terminology this reply implements both the
***Submission Response*** and the ***Filing Status.***

Case b) Filing Service with acceptable file plan

**Description  
**This example illustrates the submission of a new flight plan that is
accepted by the eASP. Having combined data acceptability and operational
acceptability into the same transaction, this means the request was
processed successfully, and the flight plan is operationally acceptable.

**  
**

**Expected FF-ICE interaction**

<img src=".//media/image244.png" style="width:4.08333in;height:1.5625in" />

<span id="_Toc498700591" class="anchor"></span>Figure 28: FF-ICE
interaction with accepted flight plan

**Example implementation**

<img src=".//media/image243.png" style="width:5.08889in;height:1.52639in" />

<span id="_Toc498700592" class="anchor"></span>Figure 29: Flight plan
filing example with accepted flight plan

-   The flightPlanSubmissionRequest contains the flight plan encoded in
    FIXM 4.1.0.

-   The flightPlanSubmissionReply contains the status ***ACK***.

-   The FilingStatusMessage contains the ***Filing Status*** with status
    ***ACCEPTABLE.***

Once again, both data acceptability and operational acceptability may be
addressed technically as part of the same transaction.

<img src=".//media/image242.png" style="width:5.11458in;height:1.55764in" />

<span id="_Toc48644019" class="anchor"></span>Figure 30: Flight plan
filing submission example with accepted (ACK and ACCEPTABLE) filed
flight plan

By doing so, the synchronous reply conveys all necessary information:
the ***ACK*** status and the accepted flight plan with the accepted
trajectory.

-   The flightPlanSubmissionReply contains the status ***ACK*** and the
    accepted flight plan encoded in FIXM 4.1.0. In FF-ICE terminology
    this reply contains both the ***Submission Response*** and the
    ***Filing Status***.

**  
**

Case c) Filing Service with manually treated flight plan

**Description  
**This example illustrates the submission of a new flight plan that is
queued for manual intervention (***MAN***).

**Expected FF-ICE interaction**

<img src=".//media/image245.png" style="width:4.08889in;height:1.60972in" />

<span id="_Toc498700593" class="anchor"></span>Figure 31: FF-ICE
interaction for manually treated flight plan

In case a flight plan submission requires manual treatment, FF-ICE
foresees a ***Submission Response***=***MAN*** followed by a subsequent
asynchronous ***Submission Response*** which could be ***ACK*** or
***REJ***, followed by an optional ***Filing Status*** that would
contain the accepted flight plan or the reasons why it was not accepted
(***NOT ACCEPTABLE***).

**Example implementation**

<img src=".//media/image246.png" style="width:5.59931in;height:1.66667in" />

<span id="_Toc498700594" class="anchor"></span>Figure 32: Flight plan
filing example with manually treated flight plan

-   The flightPlanSubmissionRequest contains the flight plan encoded in
    FIXM 4.1.0.

-   The flightPlanSubmissionReply contains the status ***MAN*** and the
    accepted flight plan encoded in FIXM 4.1.0. In FF-ICE terminology
    this reply contains both the ***Submission Response*** and the
    ***Filing Status***.

-   The FlightFilingResultMessage contains the result of the processing
    (***ACK*** or ***REJ***). In case of rejection it contains the
    reason why the flight plan was not accepted, in case of acceptance
    it contains the accepted flight plan. In practice it contains both
    the ***Submission Response*** and the ***Filing Status***.

-   The FilingStatusMessage is sent only in case the submitted flight
    plan is accepted (***ACK***) and it contains the accepted flight
    plan encoded in FIXM 4.1.0.

#### Data Implementation Description

This part will be addressed in a future version of the document.

