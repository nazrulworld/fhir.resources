#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2 on 2020-04-10.
#  2020, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """

    @classmethod
    def instantiate(cls, resource_type, jsondict, strict=True):
        """ Instantiate a resource of the type correlating to "resource_type".

        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_type:
            from . import account

            return account.Account(jsondict, strict)
        if "AccountCoverage" == resource_type:
            from . import account

            return account.AccountCoverage(jsondict, strict)
        if "AccountGuarantor" == resource_type:
            from . import account

            return account.AccountGuarantor(jsondict, strict)
        if "ActivityDefinition" == resource_type:
            from . import activitydefinition

            return activitydefinition.ActivityDefinition(jsondict, strict)
        if "ActivityDefinitionDynamicValue" == resource_type:
            from . import activitydefinition

            return activitydefinition.ActivityDefinitionDynamicValue(jsondict, strict)
        if "ActivityDefinitionParticipant" == resource_type:
            from . import activitydefinition

            return activitydefinition.ActivityDefinitionParticipant(jsondict, strict)
        if "Address" == resource_type:
            from . import address

            return address.Address(jsondict, strict)
        if "AdverseEvent" == resource_type:
            from . import adverseevent

            return adverseevent.AdverseEvent(jsondict, strict)
        if "AdverseEventSuspectEntity" == resource_type:
            from . import adverseevent

            return adverseevent.AdverseEventSuspectEntity(jsondict, strict)
        if "Age" == resource_type:
            from . import age

            return age.Age(jsondict, strict)
        if "AllergyIntolerance" == resource_type:
            from . import allergyintolerance

            return allergyintolerance.AllergyIntolerance(jsondict, strict)
        if "AllergyIntoleranceReaction" == resource_type:
            from . import allergyintolerance

            return allergyintolerance.AllergyIntoleranceReaction(jsondict, strict)
        if "Annotation" == resource_type:
            from . import annotation

            return annotation.Annotation(jsondict, strict)
        if "Appointment" == resource_type:
            from . import appointment

            return appointment.Appointment(jsondict, strict)
        if "AppointmentParticipant" == resource_type:
            from . import appointment

            return appointment.AppointmentParticipant(jsondict, strict)
        if "AppointmentResponse" == resource_type:
            from . import appointmentresponse

            return appointmentresponse.AppointmentResponse(jsondict, strict)
        if "Attachment" == resource_type:
            from . import attachment

            return attachment.Attachment(jsondict, strict)
        if "AuditEvent" == resource_type:
            from . import auditevent

            return auditevent.AuditEvent(jsondict, strict)
        if "AuditEventAgent" == resource_type:
            from . import auditevent

            return auditevent.AuditEventAgent(jsondict, strict)
        if "AuditEventAgentNetwork" == resource_type:
            from . import auditevent

            return auditevent.AuditEventAgentNetwork(jsondict, strict)
        if "AuditEventEntity" == resource_type:
            from . import auditevent

            return auditevent.AuditEventEntity(jsondict, strict)
        if "AuditEventEntityDetail" == resource_type:
            from . import auditevent

            return auditevent.AuditEventEntityDetail(jsondict, strict)
        if "AuditEventSource" == resource_type:
            from . import auditevent

            return auditevent.AuditEventSource(jsondict, strict)
        if "BackboneElement" == resource_type:
            from . import backboneelement

            return backboneelement.BackboneElement(jsondict, strict)
        if "Basic" == resource_type:
            from . import basic

            return basic.Basic(jsondict, strict)
        if "Binary" == resource_type:
            from . import binary

            return binary.Binary(jsondict, strict)
        if "BodySite" == resource_type:
            from . import bodysite

            return bodysite.BodySite(jsondict, strict)
        if "Bundle" == resource_type:
            from . import bundle

            return bundle.Bundle(jsondict, strict)
        if "BundleEntry" == resource_type:
            from . import bundle

            return bundle.BundleEntry(jsondict, strict)
        if "BundleEntryRequest" == resource_type:
            from . import bundle

            return bundle.BundleEntryRequest(jsondict, strict)
        if "BundleEntryResponse" == resource_type:
            from . import bundle

            return bundle.BundleEntryResponse(jsondict, strict)
        if "BundleEntrySearch" == resource_type:
            from . import bundle

            return bundle.BundleEntrySearch(jsondict, strict)
        if "BundleLink" == resource_type:
            from . import bundle

            return bundle.BundleLink(jsondict, strict)
        if "CapabilityStatement" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatement(jsondict, strict)
        if "CapabilityStatementDocument" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementDocument(jsondict, strict)
        if "CapabilityStatementImplementation" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementImplementation(
                jsondict, strict
            )
        if "CapabilityStatementMessaging" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessaging(jsondict, strict)
        if "CapabilityStatementMessagingEndpoint" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessagingEndpoint(
                jsondict, strict
            )
        if "CapabilityStatementMessagingEvent" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessagingEvent(
                jsondict, strict
            )
        if "CapabilityStatementMessagingSupportedMessage" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessagingSupportedMessage(
                jsondict, strict
            )
        if "CapabilityStatementRest" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRest(jsondict, strict)
        if "CapabilityStatementRestInteraction" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestInteraction(
                jsondict, strict
            )
        if "CapabilityStatementRestOperation" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestOperation(
                jsondict, strict
            )
        if "CapabilityStatementRestResource" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResource(jsondict, strict)
        if "CapabilityStatementRestResourceInteraction" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResourceInteraction(
                jsondict, strict
            )
        if "CapabilityStatementRestResourceSearchParam" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResourceSearchParam(
                jsondict, strict
            )
        if "CapabilityStatementRestSecurity" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestSecurity(jsondict, strict)
        if "CapabilityStatementRestSecurityCertificate" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestSecurityCertificate(
                jsondict, strict
            )
        if "CapabilityStatementSoftware" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementSoftware(jsondict, strict)
        if "CarePlan" == resource_type:
            from . import careplan

            return careplan.CarePlan(jsondict, strict)
        if "CarePlanActivity" == resource_type:
            from . import careplan

            return careplan.CarePlanActivity(jsondict, strict)
        if "CarePlanActivityDetail" == resource_type:
            from . import careplan

            return careplan.CarePlanActivityDetail(jsondict, strict)
        if "CareTeam" == resource_type:
            from . import careteam

            return careteam.CareTeam(jsondict, strict)
        if "CareTeamParticipant" == resource_type:
            from . import careteam

            return careteam.CareTeamParticipant(jsondict, strict)
        if "ChargeItem" == resource_type:
            from . import chargeitem

            return chargeitem.ChargeItem(jsondict, strict)
        if "ChargeItemParticipant" == resource_type:
            from . import chargeitem

            return chargeitem.ChargeItemParticipant(jsondict, strict)
        if "Claim" == resource_type:
            from . import claim

            return claim.Claim(jsondict, strict)
        if "ClaimAccident" == resource_type:
            from . import claim

            return claim.ClaimAccident(jsondict, strict)
        if "ClaimCareTeam" == resource_type:
            from . import claim

            return claim.ClaimCareTeam(jsondict, strict)
        if "ClaimDiagnosis" == resource_type:
            from . import claim

            return claim.ClaimDiagnosis(jsondict, strict)
        if "ClaimInformation" == resource_type:
            from . import claim

            return claim.ClaimInformation(jsondict, strict)
        if "ClaimInsurance" == resource_type:
            from . import claim

            return claim.ClaimInsurance(jsondict, strict)
        if "ClaimItem" == resource_type:
            from . import claim

            return claim.ClaimItem(jsondict, strict)
        if "ClaimItemDetail" == resource_type:
            from . import claim

            return claim.ClaimItemDetail(jsondict, strict)
        if "ClaimItemDetailSubDetail" == resource_type:
            from . import claim

            return claim.ClaimItemDetailSubDetail(jsondict, strict)
        if "ClaimPayee" == resource_type:
            from . import claim

            return claim.ClaimPayee(jsondict, strict)
        if "ClaimProcedure" == resource_type:
            from . import claim

            return claim.ClaimProcedure(jsondict, strict)
        if "ClaimRelated" == resource_type:
            from . import claim

            return claim.ClaimRelated(jsondict, strict)
        if "ClaimResponse" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponse(jsondict, strict)
        if "ClaimResponseAddItem" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItem(jsondict, strict)
        if "ClaimResponseAddItemDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItemDetail(jsondict, strict)
        if "ClaimResponseError" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseError(jsondict, strict)
        if "ClaimResponseInsurance" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseInsurance(jsondict, strict)
        if "ClaimResponseItem" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItem(jsondict, strict)
        if "ClaimResponseItemAdjudication" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItemAdjudication(jsondict, strict)
        if "ClaimResponseItemDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetail(jsondict, strict)
        if "ClaimResponseItemDetailSubDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict, strict)
        if "ClaimResponsePayment" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponsePayment(jsondict, strict)
        if "ClaimResponseProcessNote" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseProcessNote(jsondict, strict)
        if "ClinicalImpression" == resource_type:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpression(jsondict, strict)
        if "ClinicalImpressionFinding" == resource_type:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionFinding(jsondict, strict)
        if "ClinicalImpressionInvestigation" == resource_type:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionInvestigation(jsondict, strict)
        if "CodeSystem" == resource_type:
            from . import codesystem

            return codesystem.CodeSystem(jsondict, strict)
        if "CodeSystemConcept" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemConcept(jsondict, strict)
        if "CodeSystemConceptDesignation" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemConceptDesignation(jsondict, strict)
        if "CodeSystemConceptProperty" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemConceptProperty(jsondict, strict)
        if "CodeSystemFilter" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemFilter(jsondict, strict)
        if "CodeSystemProperty" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemProperty(jsondict, strict)
        if "CodeableConcept" == resource_type:
            from . import codeableconcept

            return codeableconcept.CodeableConcept(jsondict, strict)
        if "Coding" == resource_type:
            from . import coding

            return coding.Coding(jsondict, strict)
        if "Communication" == resource_type:
            from . import communication

            return communication.Communication(jsondict, strict)
        if "CommunicationPayload" == resource_type:
            from . import communication

            return communication.CommunicationPayload(jsondict, strict)
        if "CommunicationRequest" == resource_type:
            from . import communicationrequest

            return communicationrequest.CommunicationRequest(jsondict, strict)
        if "CommunicationRequestPayload" == resource_type:
            from . import communicationrequest

            return communicationrequest.CommunicationRequestPayload(jsondict, strict)
        if "CommunicationRequestRequester" == resource_type:
            from . import communicationrequest

            return communicationrequest.CommunicationRequestRequester(jsondict, strict)
        if "CompartmentDefinition" == resource_type:
            from . import compartmentdefinition

            return compartmentdefinition.CompartmentDefinition(jsondict, strict)
        if "CompartmentDefinitionResource" == resource_type:
            from . import compartmentdefinition

            return compartmentdefinition.CompartmentDefinitionResource(jsondict, strict)
        if "Composition" == resource_type:
            from . import composition

            return composition.Composition(jsondict, strict)
        if "CompositionAttester" == resource_type:
            from . import composition

            return composition.CompositionAttester(jsondict, strict)
        if "CompositionEvent" == resource_type:
            from . import composition

            return composition.CompositionEvent(jsondict, strict)
        if "CompositionRelatesTo" == resource_type:
            from . import composition

            return composition.CompositionRelatesTo(jsondict, strict)
        if "CompositionSection" == resource_type:
            from . import composition

            return composition.CompositionSection(jsondict, strict)
        if "ConceptMap" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMap(jsondict, strict)
        if "ConceptMapGroup" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroup(jsondict, strict)
        if "ConceptMapGroupElement" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupElement(jsondict, strict)
        if "ConceptMapGroupElementTarget" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupElementTarget(jsondict, strict)
        if "ConceptMapGroupElementTargetDependsOn" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupElementTargetDependsOn(jsondict, strict)
        if "ConceptMapGroupUnmapped" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupUnmapped(jsondict, strict)
        if "Condition" == resource_type:
            from . import condition

            return condition.Condition(jsondict, strict)
        if "ConditionEvidence" == resource_type:
            from . import condition

            return condition.ConditionEvidence(jsondict, strict)
        if "ConditionStage" == resource_type:
            from . import condition

            return condition.ConditionStage(jsondict, strict)
        if "Consent" == resource_type:
            from . import consent

            return consent.Consent(jsondict, strict)
        if "ConsentActor" == resource_type:
            from . import consent

            return consent.ConsentActor(jsondict, strict)
        if "ConsentData" == resource_type:
            from . import consent

            return consent.ConsentData(jsondict, strict)
        if "ConsentExcept" == resource_type:
            from . import consent

            return consent.ConsentExcept(jsondict, strict)
        if "ConsentExceptActor" == resource_type:
            from . import consent

            return consent.ConsentExceptActor(jsondict, strict)
        if "ConsentExceptData" == resource_type:
            from . import consent

            return consent.ConsentExceptData(jsondict, strict)
        if "ConsentPolicy" == resource_type:
            from . import consent

            return consent.ConsentPolicy(jsondict, strict)
        if "ContactDetail" == resource_type:
            from . import contactdetail

            return contactdetail.ContactDetail(jsondict, strict)
        if "ContactPoint" == resource_type:
            from . import contactpoint

            return contactpoint.ContactPoint(jsondict, strict)
        if "Contract" == resource_type:
            from . import contract

            return contract.Contract(jsondict, strict)
        if "ContractAgent" == resource_type:
            from . import contract

            return contract.ContractAgent(jsondict, strict)
        if "ContractFriendly" == resource_type:
            from . import contract

            return contract.ContractFriendly(jsondict, strict)
        if "ContractLegal" == resource_type:
            from . import contract

            return contract.ContractLegal(jsondict, strict)
        if "ContractRule" == resource_type:
            from . import contract

            return contract.ContractRule(jsondict, strict)
        if "ContractSigner" == resource_type:
            from . import contract

            return contract.ContractSigner(jsondict, strict)
        if "ContractTerm" == resource_type:
            from . import contract

            return contract.ContractTerm(jsondict, strict)
        if "ContractTermAgent" == resource_type:
            from . import contract

            return contract.ContractTermAgent(jsondict, strict)
        if "ContractTermValuedItem" == resource_type:
            from . import contract

            return contract.ContractTermValuedItem(jsondict, strict)
        if "ContractValuedItem" == resource_type:
            from . import contract

            return contract.ContractValuedItem(jsondict, strict)
        if "Contributor" == resource_type:
            from . import contributor

            return contributor.Contributor(jsondict, strict)
        if "Count" == resource_type:
            from . import count

            return count.Count(jsondict, strict)
        if "Coverage" == resource_type:
            from . import coverage

            return coverage.Coverage(jsondict, strict)
        if "CoverageGrouping" == resource_type:
            from . import coverage

            return coverage.CoverageGrouping(jsondict, strict)
        if "DataElement" == resource_type:
            from . import dataelement

            return dataelement.DataElement(jsondict, strict)
        if "DataElementMapping" == resource_type:
            from . import dataelement

            return dataelement.DataElementMapping(jsondict, strict)
        if "DataRequirement" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirement(jsondict, strict)
        if "DataRequirementCodeFilter" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirementCodeFilter(jsondict, strict)
        if "DataRequirementDateFilter" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirementDateFilter(jsondict, strict)
        if "DetectedIssue" == resource_type:
            from . import detectedissue

            return detectedissue.DetectedIssue(jsondict, strict)
        if "DetectedIssueMitigation" == resource_type:
            from . import detectedissue

            return detectedissue.DetectedIssueMitigation(jsondict, strict)
        if "Device" == resource_type:
            from . import device

            return device.Device(jsondict, strict)
        if "DeviceComponent" == resource_type:
            from . import devicecomponent

            return devicecomponent.DeviceComponent(jsondict, strict)
        if "DeviceComponentProductionSpecification" == resource_type:
            from . import devicecomponent

            return devicecomponent.DeviceComponentProductionSpecification(
                jsondict, strict
            )
        if "DeviceMetric" == resource_type:
            from . import devicemetric

            return devicemetric.DeviceMetric(jsondict, strict)
        if "DeviceMetricCalibration" == resource_type:
            from . import devicemetric

            return devicemetric.DeviceMetricCalibration(jsondict, strict)
        if "DeviceRequest" == resource_type:
            from . import devicerequest

            return devicerequest.DeviceRequest(jsondict, strict)
        if "DeviceRequestRequester" == resource_type:
            from . import devicerequest

            return devicerequest.DeviceRequestRequester(jsondict, strict)
        if "DeviceUdi" == resource_type:
            from . import device

            return device.DeviceUdi(jsondict, strict)
        if "DeviceUseStatement" == resource_type:
            from . import deviceusestatement

            return deviceusestatement.DeviceUseStatement(jsondict, strict)
        if "DiagnosticReport" == resource_type:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReport(jsondict, strict)
        if "DiagnosticReportImage" == resource_type:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReportImage(jsondict, strict)
        if "DiagnosticReportPerformer" == resource_type:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReportPerformer(jsondict, strict)
        if "Distance" == resource_type:
            from . import distance

            return distance.Distance(jsondict, strict)
        if "DocumentManifest" == resource_type:
            from . import documentmanifest

            return documentmanifest.DocumentManifest(jsondict, strict)
        if "DocumentManifestContent" == resource_type:
            from . import documentmanifest

            return documentmanifest.DocumentManifestContent(jsondict, strict)
        if "DocumentManifestRelated" == resource_type:
            from . import documentmanifest

            return documentmanifest.DocumentManifestRelated(jsondict, strict)
        if "DocumentReference" == resource_type:
            from . import documentreference

            return documentreference.DocumentReference(jsondict, strict)
        if "DocumentReferenceContent" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceContent(jsondict, strict)
        if "DocumentReferenceContext" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceContext(jsondict, strict)
        if "DocumentReferenceContextRelated" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceContextRelated(jsondict, strict)
        if "DocumentReferenceRelatesTo" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceRelatesTo(jsondict, strict)
        if "DomainResource" == resource_type:
            from . import domainresource

            return domainresource.DomainResource(jsondict, strict)
        if "Dosage" == resource_type:
            from . import dosage

            return dosage.Dosage(jsondict, strict)
        if "Duration" == resource_type:
            from . import duration

            return duration.Duration(jsondict, strict)
        if "Element" == resource_type:
            from . import element

            return element.Element(jsondict, strict)
        if "ElementDefinition" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinition(jsondict, strict)
        if "ElementDefinitionBase" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionBase(jsondict, strict)
        if "ElementDefinitionBinding" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionBinding(jsondict, strict)
        if "ElementDefinitionConstraint" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionConstraint(jsondict, strict)
        if "ElementDefinitionExample" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionExample(jsondict, strict)
        if "ElementDefinitionMapping" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionMapping(jsondict, strict)
        if "ElementDefinitionSlicing" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionSlicing(jsondict, strict)
        if "ElementDefinitionSlicingDiscriminator" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionSlicingDiscriminator(
                jsondict, strict
            )
        if "ElementDefinitionType" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionType(jsondict, strict)
        if "EligibilityRequest" == resource_type:
            from . import eligibilityrequest

            return eligibilityrequest.EligibilityRequest(jsondict, strict)
        if "EligibilityResponse" == resource_type:
            from . import eligibilityresponse

            return eligibilityresponse.EligibilityResponse(jsondict, strict)
        if "EligibilityResponseError" == resource_type:
            from . import eligibilityresponse

            return eligibilityresponse.EligibilityResponseError(jsondict, strict)
        if "EligibilityResponseInsurance" == resource_type:
            from . import eligibilityresponse

            return eligibilityresponse.EligibilityResponseInsurance(jsondict, strict)
        if "EligibilityResponseInsuranceBenefitBalance" == resource_type:
            from . import eligibilityresponse

            return eligibilityresponse.EligibilityResponseInsuranceBenefitBalance(
                jsondict, strict
            )
        if "EligibilityResponseInsuranceBenefitBalanceFinancial" == resource_type:
            from . import eligibilityresponse

            return eligibilityresponse.EligibilityResponseInsuranceBenefitBalanceFinancial(
                jsondict, strict
            )
        if "Encounter" == resource_type:
            from . import encounter

            return encounter.Encounter(jsondict, strict)
        if "EncounterClassHistory" == resource_type:
            from . import encounter

            return encounter.EncounterClassHistory(jsondict, strict)
        if "EncounterDiagnosis" == resource_type:
            from . import encounter

            return encounter.EncounterDiagnosis(jsondict, strict)
        if "EncounterHospitalization" == resource_type:
            from . import encounter

            return encounter.EncounterHospitalization(jsondict, strict)
        if "EncounterLocation" == resource_type:
            from . import encounter

            return encounter.EncounterLocation(jsondict, strict)
        if "EncounterParticipant" == resource_type:
            from . import encounter

            return encounter.EncounterParticipant(jsondict, strict)
        if "EncounterStatusHistory" == resource_type:
            from . import encounter

            return encounter.EncounterStatusHistory(jsondict, strict)
        if "Endpoint" == resource_type:
            from . import endpoint

            return endpoint.Endpoint(jsondict, strict)
        if "EnrollmentRequest" == resource_type:
            from . import enrollmentrequest

            return enrollmentrequest.EnrollmentRequest(jsondict, strict)
        if "EnrollmentResponse" == resource_type:
            from . import enrollmentresponse

            return enrollmentresponse.EnrollmentResponse(jsondict, strict)
        if "EpisodeOfCare" == resource_type:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCare(jsondict, strict)
        if "EpisodeOfCareDiagnosis" == resource_type:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCareDiagnosis(jsondict, strict)
        if "EpisodeOfCareStatusHistory" == resource_type:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCareStatusHistory(jsondict, strict)
        if "ExpansionProfile" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfile(jsondict, strict)
        if "ExpansionProfileDesignation" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileDesignation(jsondict, strict)
        if "ExpansionProfileDesignationExclude" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileDesignationExclude(jsondict, strict)
        if "ExpansionProfileDesignationExcludeDesignation" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileDesignationExcludeDesignation(
                jsondict, strict
            )
        if "ExpansionProfileDesignationInclude" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileDesignationInclude(jsondict, strict)
        if "ExpansionProfileDesignationIncludeDesignation" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileDesignationIncludeDesignation(
                jsondict, strict
            )
        if "ExpansionProfileExcludedSystem" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileExcludedSystem(jsondict, strict)
        if "ExpansionProfileFixedVersion" == resource_type:
            from . import expansionprofile

            return expansionprofile.ExpansionProfileFixedVersion(jsondict, strict)
        if "ExplanationOfBenefit" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefit(jsondict, strict)
        if "ExplanationOfBenefitAccident" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAccident(jsondict, strict)
        if "ExplanationOfBenefitAddItem" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAddItem(jsondict, strict)
        if "ExplanationOfBenefitAddItemDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAddItemDetail(
                jsondict, strict
            )
        if "ExplanationOfBenefitBenefitBalance" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitBenefitBalance(
                jsondict, strict
            )
        if "ExplanationOfBenefitBenefitBalanceFinancial" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial(
                jsondict, strict
            )
        if "ExplanationOfBenefitCareTeam" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitCareTeam(jsondict, strict)
        if "ExplanationOfBenefitDiagnosis" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitDiagnosis(jsondict, strict)
        if "ExplanationOfBenefitInformation" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitInformation(
                jsondict, strict
            )
        if "ExplanationOfBenefitInsurance" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitInsurance(jsondict, strict)
        if "ExplanationOfBenefitItem" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItem(jsondict, strict)
        if "ExplanationOfBenefitItemAdjudication" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItemAdjudication(
                jsondict, strict
            )
        if "ExplanationOfBenefitItemDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItemDetail(jsondict, strict)
        if "ExplanationOfBenefitItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail(
                jsondict, strict
            )
        if "ExplanationOfBenefitPayee" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitPayee(jsondict, strict)
        if "ExplanationOfBenefitPayment" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitPayment(jsondict, strict)
        if "ExplanationOfBenefitProcedure" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitProcedure(jsondict, strict)
        if "ExplanationOfBenefitProcessNote" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitProcessNote(
                jsondict, strict
            )
        if "ExplanationOfBenefitRelated" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitRelated(jsondict, strict)
        if "Extension" == resource_type:
            from . import extension

            return extension.Extension(jsondict, strict)
        if "FamilyMemberHistory" == resource_type:
            from . import familymemberhistory

            return familymemberhistory.FamilyMemberHistory(jsondict, strict)
        if "FamilyMemberHistoryCondition" == resource_type:
            from . import familymemberhistory

            return familymemberhistory.FamilyMemberHistoryCondition(jsondict, strict)
        if "Flag" == resource_type:
            from . import flag

            return flag.Flag(jsondict, strict)
        if "Goal" == resource_type:
            from . import goal

            return goal.Goal(jsondict, strict)
        if "GoalTarget" == resource_type:
            from . import goal

            return goal.GoalTarget(jsondict, strict)
        if "GraphDefinition" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinition(jsondict, strict)
        if "GraphDefinitionLink" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinitionLink(jsondict, strict)
        if "GraphDefinitionLinkTarget" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinitionLinkTarget(jsondict, strict)
        if "GraphDefinitionLinkTargetCompartment" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinitionLinkTargetCompartment(
                jsondict, strict
            )
        if "Group" == resource_type:
            from . import group

            return group.Group(jsondict, strict)
        if "GroupCharacteristic" == resource_type:
            from . import group

            return group.GroupCharacteristic(jsondict, strict)
        if "GroupMember" == resource_type:
            from . import group

            return group.GroupMember(jsondict, strict)
        if "GuidanceResponse" == resource_type:
            from . import guidanceresponse

            return guidanceresponse.GuidanceResponse(jsondict, strict)
        if "HealthcareService" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareService(jsondict, strict)
        if "HealthcareServiceAvailableTime" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceAvailableTime(jsondict, strict)
        if "HealthcareServiceNotAvailable" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceNotAvailable(jsondict, strict)
        if "HumanName" == resource_type:
            from . import humanname

            return humanname.HumanName(jsondict, strict)
        if "Identifier" == resource_type:
            from . import identifier

            return identifier.Identifier(jsondict, strict)
        if "ImagingManifest" == resource_type:
            from . import imagingmanifest

            return imagingmanifest.ImagingManifest(jsondict, strict)
        if "ImagingManifestStudy" == resource_type:
            from . import imagingmanifest

            return imagingmanifest.ImagingManifestStudy(jsondict, strict)
        if "ImagingManifestStudySeries" == resource_type:
            from . import imagingmanifest

            return imagingmanifest.ImagingManifestStudySeries(jsondict, strict)
        if "ImagingManifestStudySeriesInstance" == resource_type:
            from . import imagingmanifest

            return imagingmanifest.ImagingManifestStudySeriesInstance(jsondict, strict)
        if "ImagingStudy" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudy(jsondict, strict)
        if "ImagingStudySeries" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeries(jsondict, strict)
        if "ImagingStudySeriesInstance" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeriesInstance(jsondict, strict)
        if "Immunization" == resource_type:
            from . import immunization

            return immunization.Immunization(jsondict, strict)
        if "ImmunizationExplanation" == resource_type:
            from . import immunization

            return immunization.ImmunizationExplanation(jsondict, strict)
        if "ImmunizationPractitioner" == resource_type:
            from . import immunization

            return immunization.ImmunizationPractitioner(jsondict, strict)
        if "ImmunizationReaction" == resource_type:
            from . import immunization

            return immunization.ImmunizationReaction(jsondict, strict)
        if "ImmunizationRecommendation" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendation(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendation" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendation(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendationProtocol" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol(
                jsondict, strict
            )
        if "ImmunizationVaccinationProtocol" == resource_type:
            from . import immunization

            return immunization.ImmunizationVaccinationProtocol(jsondict, strict)
        if "ImplementationGuide" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuide(jsondict, strict)
        if "ImplementationGuideDependency" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDependency(jsondict, strict)
        if "ImplementationGuideGlobal" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideGlobal(jsondict, strict)
        if "ImplementationGuidePackage" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuidePackage(jsondict, strict)
        if "ImplementationGuidePackageResource" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuidePackageResource(
                jsondict, strict
            )
        if "ImplementationGuidePage" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuidePage(jsondict, strict)
        if "Library" == resource_type:
            from . import library

            return library.Library(jsondict, strict)
        if "Linkage" == resource_type:
            from . import linkage

            return linkage.Linkage(jsondict, strict)
        if "LinkageItem" == resource_type:
            from . import linkage

            return linkage.LinkageItem(jsondict, strict)
        if "List" == resource_type:
            from . import list

            return list.List(jsondict, strict)
        if "ListEntry" == resource_type:
            from . import list

            return list.ListEntry(jsondict, strict)
        if "Location" == resource_type:
            from . import location

            return location.Location(jsondict, strict)
        if "LocationPosition" == resource_type:
            from . import location

            return location.LocationPosition(jsondict, strict)
        if "Measure" == resource_type:
            from . import measure

            return measure.Measure(jsondict, strict)
        if "MeasureGroup" == resource_type:
            from . import measure

            return measure.MeasureGroup(jsondict, strict)
        if "MeasureGroupPopulation" == resource_type:
            from . import measure

            return measure.MeasureGroupPopulation(jsondict, strict)
        if "MeasureGroupStratifier" == resource_type:
            from . import measure

            return measure.MeasureGroupStratifier(jsondict, strict)
        if "MeasureReport" == resource_type:
            from . import measurereport

            return measurereport.MeasureReport(jsondict, strict)
        if "MeasureReportGroup" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroup(jsondict, strict)
        if "MeasureReportGroupPopulation" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupPopulation(jsondict, strict)
        if "MeasureReportGroupStratifier" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifier(jsondict, strict)
        if "MeasureReportGroupStratifierStratum" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifierStratum(jsondict, strict)
        if "MeasureReportGroupStratifierStratumPopulation" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifierStratumPopulation(
                jsondict, strict
            )
        if "MeasureSupplementalData" == resource_type:
            from . import measure

            return measure.MeasureSupplementalData(jsondict, strict)
        if "Media" == resource_type:
            from . import media

            return media.Media(jsondict, strict)
        if "Medication" == resource_type:
            from . import medication

            return medication.Medication(jsondict, strict)
        if "MedicationAdministration" == resource_type:
            from . import medicationadministration

            return medicationadministration.MedicationAdministration(jsondict, strict)
        if "MedicationAdministrationDosage" == resource_type:
            from . import medicationadministration

            return medicationadministration.MedicationAdministrationDosage(
                jsondict, strict
            )
        if "MedicationAdministrationPerformer" == resource_type:
            from . import medicationadministration

            return medicationadministration.MedicationAdministrationPerformer(
                jsondict, strict
            )
        if "MedicationDispense" == resource_type:
            from . import medicationdispense

            return medicationdispense.MedicationDispense(jsondict, strict)
        if "MedicationDispensePerformer" == resource_type:
            from . import medicationdispense

            return medicationdispense.MedicationDispensePerformer(jsondict, strict)
        if "MedicationDispenseSubstitution" == resource_type:
            from . import medicationdispense

            return medicationdispense.MedicationDispenseSubstitution(jsondict, strict)
        if "MedicationIngredient" == resource_type:
            from . import medication

            return medication.MedicationIngredient(jsondict, strict)
        if "MedicationPackage" == resource_type:
            from . import medication

            return medication.MedicationPackage(jsondict, strict)
        if "MedicationPackageBatch" == resource_type:
            from . import medication

            return medication.MedicationPackageBatch(jsondict, strict)
        if "MedicationPackageContent" == resource_type:
            from . import medication

            return medication.MedicationPackageContent(jsondict, strict)
        if "MedicationRequest" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequest(jsondict, strict)
        if "MedicationRequestDispenseRequest" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequestDispenseRequest(jsondict, strict)
        if "MedicationRequestRequester" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequestRequester(jsondict, strict)
        if "MedicationRequestSubstitution" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequestSubstitution(jsondict, strict)
        if "MedicationStatement" == resource_type:
            from . import medicationstatement

            return medicationstatement.MedicationStatement(jsondict, strict)
        if "MessageDefinition" == resource_type:
            from . import messagedefinition

            return messagedefinition.MessageDefinition(jsondict, strict)
        if "MessageDefinitionAllowedResponse" == resource_type:
            from . import messagedefinition

            return messagedefinition.MessageDefinitionAllowedResponse(jsondict, strict)
        if "MessageDefinitionFocus" == resource_type:
            from . import messagedefinition

            return messagedefinition.MessageDefinitionFocus(jsondict, strict)
        if "MessageHeader" == resource_type:
            from . import messageheader

            return messageheader.MessageHeader(jsondict, strict)
        if "MessageHeaderDestination" == resource_type:
            from . import messageheader

            return messageheader.MessageHeaderDestination(jsondict, strict)
        if "MessageHeaderResponse" == resource_type:
            from . import messageheader

            return messageheader.MessageHeaderResponse(jsondict, strict)
        if "MessageHeaderSource" == resource_type:
            from . import messageheader

            return messageheader.MessageHeaderSource(jsondict, strict)
        if "Meta" == resource_type:
            from . import meta

            return meta.Meta(jsondict, strict)
        if "MetadataResource" == resource_type:
            from . import metadataresource

            return metadataresource.MetadataResource(jsondict, strict)
        if "Money" == resource_type:
            from . import money

            return money.Money(jsondict, strict)
        if "NamingSystem" == resource_type:
            from . import namingsystem

            return namingsystem.NamingSystem(jsondict, strict)
        if "NamingSystemUniqueId" == resource_type:
            from . import namingsystem

            return namingsystem.NamingSystemUniqueId(jsondict, strict)
        if "Narrative" == resource_type:
            from . import narrative

            return narrative.Narrative(jsondict, strict)
        if "NutritionOrder" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrder(jsondict, strict)
        if "NutritionOrderEnteralFormula" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderEnteralFormula(jsondict, strict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderEnteralFormulaAdministration(
                jsondict, strict
            )
        if "NutritionOrderOralDiet" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDiet(jsondict, strict)
        if "NutritionOrderOralDietNutrient" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDietNutrient(jsondict, strict)
        if "NutritionOrderOralDietTexture" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDietTexture(jsondict, strict)
        if "NutritionOrderSupplement" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderSupplement(jsondict, strict)
        if "Observation" == resource_type:
            from . import observation

            return observation.Observation(jsondict, strict)
        if "ObservationComponent" == resource_type:
            from . import observation

            return observation.ObservationComponent(jsondict, strict)
        if "ObservationReferenceRange" == resource_type:
            from . import observation

            return observation.ObservationReferenceRange(jsondict, strict)
        if "ObservationRelated" == resource_type:
            from . import observation

            return observation.ObservationRelated(jsondict, strict)
        if "OperationDefinition" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinition(jsondict, strict)
        if "OperationDefinitionOverload" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionOverload(jsondict, strict)
        if "OperationDefinitionParameter" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameter(jsondict, strict)
        if "OperationDefinitionParameterBinding" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameterBinding(
                jsondict, strict
            )
        if "OperationOutcome" == resource_type:
            from . import operationoutcome

            return operationoutcome.OperationOutcome(jsondict, strict)
        if "OperationOutcomeIssue" == resource_type:
            from . import operationoutcome

            return operationoutcome.OperationOutcomeIssue(jsondict, strict)
        if "Organization" == resource_type:
            from . import organization

            return organization.Organization(jsondict, strict)
        if "OrganizationContact" == resource_type:
            from . import organization

            return organization.OrganizationContact(jsondict, strict)
        if "ParameterDefinition" == resource_type:
            from . import parameterdefinition

            return parameterdefinition.ParameterDefinition(jsondict, strict)
        if "Parameters" == resource_type:
            from . import parameters

            return parameters.Parameters(jsondict, strict)
        if "ParametersParameter" == resource_type:
            from . import parameters

            return parameters.ParametersParameter(jsondict, strict)
        if "Patient" == resource_type:
            from . import patient

            return patient.Patient(jsondict, strict)
        if "PatientAnimal" == resource_type:
            from . import patient

            return patient.PatientAnimal(jsondict, strict)
        if "PatientCommunication" == resource_type:
            from . import patient

            return patient.PatientCommunication(jsondict, strict)
        if "PatientContact" == resource_type:
            from . import patient

            return patient.PatientContact(jsondict, strict)
        if "PatientLink" == resource_type:
            from . import patient

            return patient.PatientLink(jsondict, strict)
        if "PaymentNotice" == resource_type:
            from . import paymentnotice

            return paymentnotice.PaymentNotice(jsondict, strict)
        if "PaymentReconciliation" == resource_type:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliation(jsondict, strict)
        if "PaymentReconciliationDetail" == resource_type:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliationDetail(jsondict, strict)
        if "PaymentReconciliationProcessNote" == resource_type:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliationProcessNote(
                jsondict, strict
            )
        if "Period" == resource_type:
            from . import period

            return period.Period(jsondict, strict)
        if "Person" == resource_type:
            from . import person

            return person.Person(jsondict, strict)
        if "PersonLink" == resource_type:
            from . import person

            return person.PersonLink(jsondict, strict)
        if "PlanDefinition" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinition(jsondict, strict)
        if "PlanDefinitionAction" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionAction(jsondict, strict)
        if "PlanDefinitionActionCondition" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionCondition(jsondict, strict)
        if "PlanDefinitionActionDynamicValue" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionDynamicValue(jsondict, strict)
        if "PlanDefinitionActionParticipant" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionParticipant(jsondict, strict)
        if "PlanDefinitionActionRelatedAction" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionRelatedAction(jsondict, strict)
        if "PlanDefinitionGoal" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionGoal(jsondict, strict)
        if "PlanDefinitionGoalTarget" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionGoalTarget(jsondict, strict)
        if "Practitioner" == resource_type:
            from . import practitioner

            return practitioner.Practitioner(jsondict, strict)
        if "PractitionerQualification" == resource_type:
            from . import practitioner

            return practitioner.PractitionerQualification(jsondict, strict)
        if "PractitionerRole" == resource_type:
            from . import practitionerrole

            return practitionerrole.PractitionerRole(jsondict, strict)
        if "PractitionerRoleAvailableTime" == resource_type:
            from . import practitionerrole

            return practitionerrole.PractitionerRoleAvailableTime(jsondict, strict)
        if "PractitionerRoleNotAvailable" == resource_type:
            from . import practitionerrole

            return practitionerrole.PractitionerRoleNotAvailable(jsondict, strict)
        if "Procedure" == resource_type:
            from . import procedure

            return procedure.Procedure(jsondict, strict)
        if "ProcedureFocalDevice" == resource_type:
            from . import procedure

            return procedure.ProcedureFocalDevice(jsondict, strict)
        if "ProcedurePerformer" == resource_type:
            from . import procedure

            return procedure.ProcedurePerformer(jsondict, strict)
        if "ProcedureRequest" == resource_type:
            from . import procedurerequest

            return procedurerequest.ProcedureRequest(jsondict, strict)
        if "ProcedureRequestRequester" == resource_type:
            from . import procedurerequest

            return procedurerequest.ProcedureRequestRequester(jsondict, strict)
        if "ProcessRequest" == resource_type:
            from . import processrequest

            return processrequest.ProcessRequest(jsondict, strict)
        if "ProcessRequestItem" == resource_type:
            from . import processrequest

            return processrequest.ProcessRequestItem(jsondict, strict)
        if "ProcessResponse" == resource_type:
            from . import processresponse

            return processresponse.ProcessResponse(jsondict, strict)
        if "ProcessResponseProcessNote" == resource_type:
            from . import processresponse

            return processresponse.ProcessResponseProcessNote(jsondict, strict)
        if "Provenance" == resource_type:
            from . import provenance

            return provenance.Provenance(jsondict, strict)
        if "ProvenanceAgent" == resource_type:
            from . import provenance

            return provenance.ProvenanceAgent(jsondict, strict)
        if "ProvenanceEntity" == resource_type:
            from . import provenance

            return provenance.ProvenanceEntity(jsondict, strict)
        if "Quantity" == resource_type:
            from . import quantity

            return quantity.Quantity(jsondict, strict)
        if "Questionnaire" == resource_type:
            from . import questionnaire

            return questionnaire.Questionnaire(jsondict, strict)
        if "QuestionnaireItem" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItem(jsondict, strict)
        if "QuestionnaireItemEnableWhen" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItemEnableWhen(jsondict, strict)
        if "QuestionnaireItemOption" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItemOption(jsondict, strict)
        if "QuestionnaireResponse" == resource_type:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponse(jsondict, strict)
        if "QuestionnaireResponseItem" == resource_type:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseItem(jsondict, strict)
        if "QuestionnaireResponseItemAnswer" == resource_type:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseItemAnswer(
                jsondict, strict
            )
        if "Range" == resource_type:
            from . import range

            return range.Range(jsondict, strict)
        if "Ratio" == resource_type:
            from . import ratio

            return ratio.Ratio(jsondict, strict)
        if "Reference" == resource_type:
            from . import reference

            return reference.Reference(jsondict, strict)
        if "ReferralRequest" == resource_type:
            from . import referralrequest

            return referralrequest.ReferralRequest(jsondict, strict)
        if "ReferralRequestRequester" == resource_type:
            from . import referralrequest

            return referralrequest.ReferralRequestRequester(jsondict, strict)
        if "RelatedArtifact" == resource_type:
            from . import relatedartifact

            return relatedartifact.RelatedArtifact(jsondict, strict)
        if "RelatedPerson" == resource_type:
            from . import relatedperson

            return relatedperson.RelatedPerson(jsondict, strict)
        if "RequestGroup" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroup(jsondict, strict)
        if "RequestGroupAction" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroupAction(jsondict, strict)
        if "RequestGroupActionCondition" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroupActionCondition(jsondict, strict)
        if "RequestGroupActionRelatedAction" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroupActionRelatedAction(jsondict, strict)
        if "ResearchStudy" == resource_type:
            from . import researchstudy

            return researchstudy.ResearchStudy(jsondict, strict)
        if "ResearchStudyArm" == resource_type:
            from . import researchstudy

            return researchstudy.ResearchStudyArm(jsondict, strict)
        if "ResearchSubject" == resource_type:
            from . import researchsubject

            return researchsubject.ResearchSubject(jsondict, strict)
        if "Resource" == resource_type:
            from . import resource

            return resource.Resource(jsondict, strict)
        if "RiskAssessment" == resource_type:
            from . import riskassessment

            return riskassessment.RiskAssessment(jsondict, strict)
        if "RiskAssessmentPrediction" == resource_type:
            from . import riskassessment

            return riskassessment.RiskAssessmentPrediction(jsondict, strict)
        if "SampledData" == resource_type:
            from . import sampleddata

            return sampleddata.SampledData(jsondict, strict)
        if "Schedule" == resource_type:
            from . import schedule

            return schedule.Schedule(jsondict, strict)
        if "SearchParameter" == resource_type:
            from . import searchparameter

            return searchparameter.SearchParameter(jsondict, strict)
        if "SearchParameterComponent" == resource_type:
            from . import searchparameter

            return searchparameter.SearchParameterComponent(jsondict, strict)
        if "Sequence" == resource_type:
            from . import sequence

            return sequence.Sequence(jsondict, strict)
        if "SequenceQuality" == resource_type:
            from . import sequence

            return sequence.SequenceQuality(jsondict, strict)
        if "SequenceReferenceSeq" == resource_type:
            from . import sequence

            return sequence.SequenceReferenceSeq(jsondict, strict)
        if "SequenceRepository" == resource_type:
            from . import sequence

            return sequence.SequenceRepository(jsondict, strict)
        if "SequenceVariant" == resource_type:
            from . import sequence

            return sequence.SequenceVariant(jsondict, strict)
        if "ServiceDefinition" == resource_type:
            from . import servicedefinition

            return servicedefinition.ServiceDefinition(jsondict, strict)
        if "Signature" == resource_type:
            from . import signature

            return signature.Signature(jsondict, strict)
        if "Slot" == resource_type:
            from . import slot

            return slot.Slot(jsondict, strict)
        if "Specimen" == resource_type:
            from . import specimen

            return specimen.Specimen(jsondict, strict)
        if "SpecimenCollection" == resource_type:
            from . import specimen

            return specimen.SpecimenCollection(jsondict, strict)
        if "SpecimenContainer" == resource_type:
            from . import specimen

            return specimen.SpecimenContainer(jsondict, strict)
        if "SpecimenProcessing" == resource_type:
            from . import specimen

            return specimen.SpecimenProcessing(jsondict, strict)
        if "StructureDefinition" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinition(jsondict, strict)
        if "StructureDefinitionDifferential" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionDifferential(jsondict, strict)
        if "StructureDefinitionMapping" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionMapping(jsondict, strict)
        if "StructureDefinitionSnapshot" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionSnapshot(jsondict, strict)
        if "StructureMap" == resource_type:
            from . import structuremap

            return structuremap.StructureMap(jsondict, strict)
        if "StructureMapGroup" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroup(jsondict, strict)
        if "StructureMapGroupInput" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupInput(jsondict, strict)
        if "StructureMapGroupRule" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRule(jsondict, strict)
        if "StructureMapGroupRuleDependent" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleDependent(jsondict, strict)
        if "StructureMapGroupRuleSource" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleSource(jsondict, strict)
        if "StructureMapGroupRuleTarget" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleTarget(jsondict, strict)
        if "StructureMapGroupRuleTargetParameter" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleTargetParameter(jsondict, strict)
        if "StructureMapStructure" == resource_type:
            from . import structuremap

            return structuremap.StructureMapStructure(jsondict, strict)
        if "Subscription" == resource_type:
            from . import subscription

            return subscription.Subscription(jsondict, strict)
        if "SubscriptionChannel" == resource_type:
            from . import subscription

            return subscription.SubscriptionChannel(jsondict, strict)
        if "Substance" == resource_type:
            from . import substance

            return substance.Substance(jsondict, strict)
        if "SubstanceIngredient" == resource_type:
            from . import substance

            return substance.SubstanceIngredient(jsondict, strict)
        if "SubstanceInstance" == resource_type:
            from . import substance

            return substance.SubstanceInstance(jsondict, strict)
        if "SupplyDelivery" == resource_type:
            from . import supplydelivery

            return supplydelivery.SupplyDelivery(jsondict, strict)
        if "SupplyDeliverySuppliedItem" == resource_type:
            from . import supplydelivery

            return supplydelivery.SupplyDeliverySuppliedItem(jsondict, strict)
        if "SupplyRequest" == resource_type:
            from . import supplyrequest

            return supplyrequest.SupplyRequest(jsondict, strict)
        if "SupplyRequestOrderedItem" == resource_type:
            from . import supplyrequest

            return supplyrequest.SupplyRequestOrderedItem(jsondict, strict)
        if "SupplyRequestRequester" == resource_type:
            from . import supplyrequest

            return supplyrequest.SupplyRequestRequester(jsondict, strict)
        if "Task" == resource_type:
            from . import task

            return task.Task(jsondict, strict)
        if "TaskInput" == resource_type:
            from . import task

            return task.TaskInput(jsondict, strict)
        if "TaskOutput" == resource_type:
            from . import task

            return task.TaskOutput(jsondict, strict)
        if "TaskRequester" == resource_type:
            from . import task

            return task.TaskRequester(jsondict, strict)
        if "TaskRestriction" == resource_type:
            from . import task

            return task.TaskRestriction(jsondict, strict)
        if "TestReport" == resource_type:
            from . import testreport

            return testreport.TestReport(jsondict, strict)
        if "TestReportParticipant" == resource_type:
            from . import testreport

            return testreport.TestReportParticipant(jsondict, strict)
        if "TestReportSetup" == resource_type:
            from . import testreport

            return testreport.TestReportSetup(jsondict, strict)
        if "TestReportSetupAction" == resource_type:
            from . import testreport

            return testreport.TestReportSetupAction(jsondict, strict)
        if "TestReportSetupActionAssert" == resource_type:
            from . import testreport

            return testreport.TestReportSetupActionAssert(jsondict, strict)
        if "TestReportSetupActionOperation" == resource_type:
            from . import testreport

            return testreport.TestReportSetupActionOperation(jsondict, strict)
        if "TestReportTeardown" == resource_type:
            from . import testreport

            return testreport.TestReportTeardown(jsondict, strict)
        if "TestReportTeardownAction" == resource_type:
            from . import testreport

            return testreport.TestReportTeardownAction(jsondict, strict)
        if "TestReportTest" == resource_type:
            from . import testreport

            return testreport.TestReportTest(jsondict, strict)
        if "TestReportTestAction" == resource_type:
            from . import testreport

            return testreport.TestReportTestAction(jsondict, strict)
        if "TestScript" == resource_type:
            from . import testscript

            return testscript.TestScript(jsondict, strict)
        if "TestScriptDestination" == resource_type:
            from . import testscript

            return testscript.TestScriptDestination(jsondict, strict)
        if "TestScriptFixture" == resource_type:
            from . import testscript

            return testscript.TestScriptFixture(jsondict, strict)
        if "TestScriptMetadata" == resource_type:
            from . import testscript

            return testscript.TestScriptMetadata(jsondict, strict)
        if "TestScriptMetadataCapability" == resource_type:
            from . import testscript

            return testscript.TestScriptMetadataCapability(jsondict, strict)
        if "TestScriptMetadataLink" == resource_type:
            from . import testscript

            return testscript.TestScriptMetadataLink(jsondict, strict)
        if "TestScriptOrigin" == resource_type:
            from . import testscript

            return testscript.TestScriptOrigin(jsondict, strict)
        if "TestScriptRule" == resource_type:
            from . import testscript

            return testscript.TestScriptRule(jsondict, strict)
        if "TestScriptRuleParam" == resource_type:
            from . import testscript

            return testscript.TestScriptRuleParam(jsondict, strict)
        if "TestScriptRuleset" == resource_type:
            from . import testscript

            return testscript.TestScriptRuleset(jsondict, strict)
        if "TestScriptRulesetRule" == resource_type:
            from . import testscript

            return testscript.TestScriptRulesetRule(jsondict, strict)
        if "TestScriptRulesetRuleParam" == resource_type:
            from . import testscript

            return testscript.TestScriptRulesetRuleParam(jsondict, strict)
        if "TestScriptSetup" == resource_type:
            from . import testscript

            return testscript.TestScriptSetup(jsondict, strict)
        if "TestScriptSetupAction" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupAction(jsondict, strict)
        if "TestScriptSetupActionAssert" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssert(jsondict, strict)
        if "TestScriptSetupActionAssertRule" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssertRule(jsondict, strict)
        if "TestScriptSetupActionAssertRuleParam" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssertRuleParam(jsondict, strict)
        if "TestScriptSetupActionAssertRuleset" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssertRuleset(jsondict, strict)
        if "TestScriptSetupActionAssertRulesetRule" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssertRulesetRule(jsondict, strict)
        if "TestScriptSetupActionAssertRulesetRuleParam" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssertRulesetRuleParam(
                jsondict, strict
            )
        if "TestScriptSetupActionOperation" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionOperation(jsondict, strict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionOperationRequestHeader(
                jsondict, strict
            )
        if "TestScriptTeardown" == resource_type:
            from . import testscript

            return testscript.TestScriptTeardown(jsondict, strict)
        if "TestScriptTeardownAction" == resource_type:
            from . import testscript

            return testscript.TestScriptTeardownAction(jsondict, strict)
        if "TestScriptTest" == resource_type:
            from . import testscript

            return testscript.TestScriptTest(jsondict, strict)
        if "TestScriptTestAction" == resource_type:
            from . import testscript

            return testscript.TestScriptTestAction(jsondict, strict)
        if "TestScriptVariable" == resource_type:
            from . import testscript

            return testscript.TestScriptVariable(jsondict, strict)
        if "Timing" == resource_type:
            from . import timing

            return timing.Timing(jsondict, strict)
        if "TimingRepeat" == resource_type:
            from . import timing

            return timing.TimingRepeat(jsondict, strict)
        if "TriggerDefinition" == resource_type:
            from . import triggerdefinition

            return triggerdefinition.TriggerDefinition(jsondict, strict)
        if "UsageContext" == resource_type:
            from . import usagecontext

            return usagecontext.UsageContext(jsondict, strict)
        if "ValueSet" == resource_type:
            from . import valueset

            return valueset.ValueSet(jsondict, strict)
        if "ValueSetCompose" == resource_type:
            from . import valueset

            return valueset.ValueSetCompose(jsondict, strict)
        if "ValueSetComposeInclude" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeInclude(jsondict, strict)
        if "ValueSetComposeIncludeConcept" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeIncludeConcept(jsondict, strict)
        if "ValueSetComposeIncludeConceptDesignation" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeIncludeConceptDesignation(jsondict, strict)
        if "ValueSetComposeIncludeFilter" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeIncludeFilter(jsondict, strict)
        if "ValueSetExpansion" == resource_type:
            from . import valueset

            return valueset.ValueSetExpansion(jsondict, strict)
        if "ValueSetExpansionContains" == resource_type:
            from . import valueset

            return valueset.ValueSetExpansionContains(jsondict, strict)
        if "ValueSetExpansionParameter" == resource_type:
            from . import valueset

            return valueset.ValueSetExpansionParameter(jsondict, strict)
        if "VisionPrescription" == resource_type:
            from . import visionprescription

            return visionprescription.VisionPrescription(jsondict, strict)
        if "VisionPrescriptionDispense" == resource_type:
            from . import visionprescription

            return visionprescription.VisionPrescriptionDispense(jsondict, strict)
        from . import element

        return element.Element(jsondict, strict)
