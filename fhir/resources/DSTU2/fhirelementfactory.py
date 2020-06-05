#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """

    @classmethod
    def instantiate(cls, resource_name, jsondict, strict=True):
        """ Instantiate a resource of the type correlating to "resource_name".

        :param str resource_name: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_name:
            from . import account

            return account.Account(jsondict, strict)
        if "Address" == resource_name:
            from . import address

            return address.Address(jsondict, strict)
        if "Age" == resource_name:
            from . import age

            return age.Age(jsondict, strict)
        if "AllergyIntolerance" == resource_name:
            from . import allergyintolerance

            return allergyintolerance.AllergyIntolerance(jsondict, strict)
        if "AllergyIntoleranceReaction" == resource_name:
            from . import allergyintolerance

            return allergyintolerance.AllergyIntoleranceReaction(jsondict, strict)
        if "Annotation" == resource_name:
            from . import annotation

            return annotation.Annotation(jsondict, strict)
        if "Appointment" == resource_name:
            from . import appointment

            return appointment.Appointment(jsondict, strict)
        if "AppointmentParticipant" == resource_name:
            from . import appointment

            return appointment.AppointmentParticipant(jsondict, strict)
        if "AppointmentResponse" == resource_name:
            from . import appointmentresponse

            return appointmentresponse.AppointmentResponse(jsondict, strict)
        if "Attachment" == resource_name:
            from . import attachment

            return attachment.Attachment(jsondict, strict)
        if "AuditEvent" == resource_name:
            from . import auditevent

            return auditevent.AuditEvent(jsondict, strict)
        if "AuditEventEvent" == resource_name:
            from . import auditevent

            return auditevent.AuditEventEvent(jsondict, strict)
        if "AuditEventObject" == resource_name:
            from . import auditevent

            return auditevent.AuditEventObject(jsondict, strict)
        if "AuditEventObjectDetail" == resource_name:
            from . import auditevent

            return auditevent.AuditEventObjectDetail(jsondict, strict)
        if "AuditEventParticipant" == resource_name:
            from . import auditevent

            return auditevent.AuditEventParticipant(jsondict, strict)
        if "AuditEventParticipantNetwork" == resource_name:
            from . import auditevent

            return auditevent.AuditEventParticipantNetwork(jsondict, strict)
        if "AuditEventSource" == resource_name:
            from . import auditevent

            return auditevent.AuditEventSource(jsondict, strict)
        if "BackboneElement" == resource_name:
            from . import backboneelement

            return backboneelement.BackboneElement(jsondict, strict)
        if "Basic" == resource_name:
            from . import basic

            return basic.Basic(jsondict, strict)
        if "Binary" == resource_name:
            from . import binary

            return binary.Binary(jsondict, strict)
        if "BodySite" == resource_name:
            from . import bodysite

            return bodysite.BodySite(jsondict, strict)
        if "Bundle" == resource_name:
            from . import bundle

            return bundle.Bundle(jsondict, strict)
        if "BundleEntry" == resource_name:
            from . import bundle

            return bundle.BundleEntry(jsondict, strict)
        if "BundleEntryRequest" == resource_name:
            from . import bundle

            return bundle.BundleEntryRequest(jsondict, strict)
        if "BundleEntryResponse" == resource_name:
            from . import bundle

            return bundle.BundleEntryResponse(jsondict, strict)
        if "BundleEntrySearch" == resource_name:
            from . import bundle

            return bundle.BundleEntrySearch(jsondict, strict)
        if "BundleLink" == resource_name:
            from . import bundle

            return bundle.BundleLink(jsondict, strict)
        if "CarePlan" == resource_name:
            from . import careplan

            return careplan.CarePlan(jsondict, strict)
        if "CarePlanActivity" == resource_name:
            from . import careplan

            return careplan.CarePlanActivity(jsondict, strict)
        if "CarePlanActivityDetail" == resource_name:
            from . import careplan

            return careplan.CarePlanActivityDetail(jsondict, strict)
        if "CarePlanParticipant" == resource_name:
            from . import careplan

            return careplan.CarePlanParticipant(jsondict, strict)
        if "CarePlanRelatedPlan" == resource_name:
            from . import careplan

            return careplan.CarePlanRelatedPlan(jsondict, strict)
        if "Claim" == resource_name:
            from . import claim

            return claim.Claim(jsondict, strict)
        if "ClaimCoverage" == resource_name:
            from . import claim

            return claim.ClaimCoverage(jsondict, strict)
        if "ClaimDiagnosis" == resource_name:
            from . import claim

            return claim.ClaimDiagnosis(jsondict, strict)
        if "ClaimItem" == resource_name:
            from . import claim

            return claim.ClaimItem(jsondict, strict)
        if "ClaimItemDetail" == resource_name:
            from . import claim

            return claim.ClaimItemDetail(jsondict, strict)
        if "ClaimItemDetailSubDetail" == resource_name:
            from . import claim

            return claim.ClaimItemDetailSubDetail(jsondict, strict)
        if "ClaimItemProsthesis" == resource_name:
            from . import claim

            return claim.ClaimItemProsthesis(jsondict, strict)
        if "ClaimMissingTeeth" == resource_name:
            from . import claim

            return claim.ClaimMissingTeeth(jsondict, strict)
        if "ClaimPayee" == resource_name:
            from . import claim

            return claim.ClaimPayee(jsondict, strict)
        if "ClaimResponse" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponse(jsondict, strict)
        if "ClaimResponseAddItem" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItem(jsondict, strict)
        if "ClaimResponseAddItemAdjudication" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItemAdjudication(jsondict, strict)
        if "ClaimResponseAddItemDetail" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItemDetail(jsondict, strict)
        if "ClaimResponseAddItemDetailAdjudication" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItemDetailAdjudication(
                jsondict, strict
            )
        if "ClaimResponseCoverage" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseCoverage(jsondict, strict)
        if "ClaimResponseError" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseError(jsondict, strict)
        if "ClaimResponseItem" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseItem(jsondict, strict)
        if "ClaimResponseItemAdjudication" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseItemAdjudication(jsondict, strict)
        if "ClaimResponseItemDetail" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetail(jsondict, strict)
        if "ClaimResponseItemDetailAdjudication" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetailAdjudication(jsondict, strict)
        if "ClaimResponseItemDetailSubDetail" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict, strict)
        if "ClaimResponseItemDetailSubDetailAdjudication" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetailSubDetailAdjudication(
                jsondict, strict
            )
        if "ClaimResponseNote" == resource_name:
            from . import claimresponse

            return claimresponse.ClaimResponseNote(jsondict, strict)
        if "ClinicalImpression" == resource_name:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpression(jsondict, strict)
        if "ClinicalImpressionFinding" == resource_name:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionFinding(jsondict, strict)
        if "ClinicalImpressionInvestigations" == resource_name:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionInvestigations(jsondict, strict)
        if "ClinicalImpressionRuledOut" == resource_name:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionRuledOut(jsondict, strict)
        if "CodeableConcept" == resource_name:
            from . import codeableconcept

            return codeableconcept.CodeableConcept(jsondict, strict)
        if "Coding" == resource_name:
            from . import coding

            return coding.Coding(jsondict, strict)
        if "Communication" == resource_name:
            from . import communication

            return communication.Communication(jsondict, strict)
        if "CommunicationPayload" == resource_name:
            from . import communication

            return communication.CommunicationPayload(jsondict, strict)
        if "CommunicationRequest" == resource_name:
            from . import communicationrequest

            return communicationrequest.CommunicationRequest(jsondict, strict)
        if "CommunicationRequestPayload" == resource_name:
            from . import communicationrequest

            return communicationrequest.CommunicationRequestPayload(jsondict, strict)
        if "Composition" == resource_name:
            from . import composition

            return composition.Composition(jsondict, strict)
        if "CompositionAttester" == resource_name:
            from . import composition

            return composition.CompositionAttester(jsondict, strict)
        if "CompositionEvent" == resource_name:
            from . import composition

            return composition.CompositionEvent(jsondict, strict)
        if "CompositionSection" == resource_name:
            from . import composition

            return composition.CompositionSection(jsondict, strict)
        if "ConceptMap" == resource_name:
            from . import conceptmap

            return conceptmap.ConceptMap(jsondict, strict)
        if "ConceptMapContact" == resource_name:
            from . import conceptmap

            return conceptmap.ConceptMapContact(jsondict, strict)
        if "ConceptMapElement" == resource_name:
            from . import conceptmap

            return conceptmap.ConceptMapElement(jsondict, strict)
        if "ConceptMapElementTarget" == resource_name:
            from . import conceptmap

            return conceptmap.ConceptMapElementTarget(jsondict, strict)
        if "ConceptMapElementTargetDependsOn" == resource_name:
            from . import conceptmap

            return conceptmap.ConceptMapElementTargetDependsOn(jsondict, strict)
        if "Condition" == resource_name:
            from . import condition

            return condition.Condition(jsondict, strict)
        if "ConditionEvidence" == resource_name:
            from . import condition

            return condition.ConditionEvidence(jsondict, strict)
        if "ConditionStage" == resource_name:
            from . import condition

            return condition.ConditionStage(jsondict, strict)
        if "Conformance" == resource_name:
            from . import conformance

            return conformance.Conformance(jsondict, strict)
        if "ConformanceContact" == resource_name:
            from . import conformance

            return conformance.ConformanceContact(jsondict, strict)
        if "ConformanceDocument" == resource_name:
            from . import conformance

            return conformance.ConformanceDocument(jsondict, strict)
        if "ConformanceImplementation" == resource_name:
            from . import conformance

            return conformance.ConformanceImplementation(jsondict, strict)
        if "ConformanceMessaging" == resource_name:
            from . import conformance

            return conformance.ConformanceMessaging(jsondict, strict)
        if "ConformanceMessagingEndpoint" == resource_name:
            from . import conformance

            return conformance.ConformanceMessagingEndpoint(jsondict, strict)
        if "ConformanceMessagingEvent" == resource_name:
            from . import conformance

            return conformance.ConformanceMessagingEvent(jsondict, strict)
        if "ConformanceRest" == resource_name:
            from . import conformance

            return conformance.ConformanceRest(jsondict, strict)
        if "ConformanceRestInteraction" == resource_name:
            from . import conformance

            return conformance.ConformanceRestInteraction(jsondict, strict)
        if "ConformanceRestOperation" == resource_name:
            from . import conformance

            return conformance.ConformanceRestOperation(jsondict, strict)
        if "ConformanceRestResource" == resource_name:
            from . import conformance

            return conformance.ConformanceRestResource(jsondict, strict)
        if "ConformanceRestResourceInteraction" == resource_name:
            from . import conformance

            return conformance.ConformanceRestResourceInteraction(jsondict, strict)
        if "ConformanceRestResourceSearchParam" == resource_name:
            from . import conformance

            return conformance.ConformanceRestResourceSearchParam(jsondict, strict)
        if "ConformanceRestSecurity" == resource_name:
            from . import conformance

            return conformance.ConformanceRestSecurity(jsondict, strict)
        if "ConformanceRestSecurityCertificate" == resource_name:
            from . import conformance

            return conformance.ConformanceRestSecurityCertificate(jsondict, strict)
        if "ConformanceSoftware" == resource_name:
            from . import conformance

            return conformance.ConformanceSoftware(jsondict, strict)
        if "ContactPoint" == resource_name:
            from . import contactpoint

            return contactpoint.ContactPoint(jsondict, strict)
        if "Contract" == resource_name:
            from . import contract

            return contract.Contract(jsondict, strict)
        if "ContractActor" == resource_name:
            from . import contract

            return contract.ContractActor(jsondict, strict)
        if "ContractFriendly" == resource_name:
            from . import contract

            return contract.ContractFriendly(jsondict, strict)
        if "ContractLegal" == resource_name:
            from . import contract

            return contract.ContractLegal(jsondict, strict)
        if "ContractRule" == resource_name:
            from . import contract

            return contract.ContractRule(jsondict, strict)
        if "ContractSigner" == resource_name:
            from . import contract

            return contract.ContractSigner(jsondict, strict)
        if "ContractTerm" == resource_name:
            from . import contract

            return contract.ContractTerm(jsondict, strict)
        if "ContractTermActor" == resource_name:
            from . import contract

            return contract.ContractTermActor(jsondict, strict)
        if "ContractTermValuedItem" == resource_name:
            from . import contract

            return contract.ContractTermValuedItem(jsondict, strict)
        if "ContractValuedItem" == resource_name:
            from . import contract

            return contract.ContractValuedItem(jsondict, strict)
        if "Count" == resource_name:
            from . import count

            return count.Count(jsondict, strict)
        if "Coverage" == resource_name:
            from . import coverage

            return coverage.Coverage(jsondict, strict)
        if "DataElement" == resource_name:
            from . import dataelement

            return dataelement.DataElement(jsondict, strict)
        if "DataElementContact" == resource_name:
            from . import dataelement

            return dataelement.DataElementContact(jsondict, strict)
        if "DataElementMapping" == resource_name:
            from . import dataelement

            return dataelement.DataElementMapping(jsondict, strict)
        if "DetectedIssue" == resource_name:
            from . import detectedissue

            return detectedissue.DetectedIssue(jsondict, strict)
        if "DetectedIssueMitigation" == resource_name:
            from . import detectedissue

            return detectedissue.DetectedIssueMitigation(jsondict, strict)
        if "Device" == resource_name:
            from . import device

            return device.Device(jsondict, strict)
        if "DeviceComponent" == resource_name:
            from . import devicecomponent

            return devicecomponent.DeviceComponent(jsondict, strict)
        if "DeviceComponentProductionSpecification" == resource_name:
            from . import devicecomponent

            return devicecomponent.DeviceComponentProductionSpecification(
                jsondict, strict
            )
        if "DeviceMetric" == resource_name:
            from . import devicemetric

            return devicemetric.DeviceMetric(jsondict, strict)
        if "DeviceMetricCalibration" == resource_name:
            from . import devicemetric

            return devicemetric.DeviceMetricCalibration(jsondict, strict)
        if "DeviceUseRequest" == resource_name:
            from . import deviceuserequest

            return deviceuserequest.DeviceUseRequest(jsondict, strict)
        if "DeviceUseStatement" == resource_name:
            from . import deviceusestatement

            return deviceusestatement.DeviceUseStatement(jsondict, strict)
        if "DiagnosticOrder" == resource_name:
            from . import diagnosticorder

            return diagnosticorder.DiagnosticOrder(jsondict, strict)
        if "DiagnosticOrderEvent" == resource_name:
            from . import diagnosticorder

            return diagnosticorder.DiagnosticOrderEvent(jsondict, strict)
        if "DiagnosticOrderItem" == resource_name:
            from . import diagnosticorder

            return diagnosticorder.DiagnosticOrderItem(jsondict, strict)
        if "DiagnosticReport" == resource_name:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReport(jsondict, strict)
        if "DiagnosticReportImage" == resource_name:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReportImage(jsondict, strict)
        if "Distance" == resource_name:
            from . import distance

            return distance.Distance(jsondict, strict)
        if "DocumentManifest" == resource_name:
            from . import documentmanifest

            return documentmanifest.DocumentManifest(jsondict, strict)
        if "DocumentManifestContent" == resource_name:
            from . import documentmanifest

            return documentmanifest.DocumentManifestContent(jsondict, strict)
        if "DocumentManifestRelated" == resource_name:
            from . import documentmanifest

            return documentmanifest.DocumentManifestRelated(jsondict, strict)
        if "DocumentReference" == resource_name:
            from . import documentreference

            return documentreference.DocumentReference(jsondict, strict)
        if "DocumentReferenceContent" == resource_name:
            from . import documentreference

            return documentreference.DocumentReferenceContent(jsondict, strict)
        if "DocumentReferenceContext" == resource_name:
            from . import documentreference

            return documentreference.DocumentReferenceContext(jsondict, strict)
        if "DocumentReferenceContextRelated" == resource_name:
            from . import documentreference

            return documentreference.DocumentReferenceContextRelated(jsondict, strict)
        if "DocumentReferenceRelatesTo" == resource_name:
            from . import documentreference

            return documentreference.DocumentReferenceRelatesTo(jsondict, strict)
        if "DomainResource" == resource_name:
            from . import domainresource

            return domainresource.DomainResource(jsondict, strict)
        if "Duration" == resource_name:
            from . import duration

            return duration.Duration(jsondict, strict)
        if "Element" == resource_name:
            from . import element

            return element.Element(jsondict, strict)
        if "ElementDefinition" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinition(jsondict, strict)
        if "ElementDefinitionBase" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionBase(jsondict, strict)
        if "ElementDefinitionBinding" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionBinding(jsondict, strict)
        if "ElementDefinitionConstraint" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionConstraint(jsondict, strict)
        if "ElementDefinitionMapping" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionMapping(jsondict, strict)
        if "ElementDefinitionSlicing" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionSlicing(jsondict, strict)
        if "ElementDefinitionType" == resource_name:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionType(jsondict, strict)
        if "EligibilityRequest" == resource_name:
            from . import eligibilityrequest

            return eligibilityrequest.EligibilityRequest(jsondict, strict)
        if "EligibilityResponse" == resource_name:
            from . import eligibilityresponse

            return eligibilityresponse.EligibilityResponse(jsondict, strict)
        if "Encounter" == resource_name:
            from . import encounter

            return encounter.Encounter(jsondict, strict)
        if "EncounterHospitalization" == resource_name:
            from . import encounter

            return encounter.EncounterHospitalization(jsondict, strict)
        if "EncounterLocation" == resource_name:
            from . import encounter

            return encounter.EncounterLocation(jsondict, strict)
        if "EncounterParticipant" == resource_name:
            from . import encounter

            return encounter.EncounterParticipant(jsondict, strict)
        if "EncounterStatusHistory" == resource_name:
            from . import encounter

            return encounter.EncounterStatusHistory(jsondict, strict)
        if "EnrollmentRequest" == resource_name:
            from . import enrollmentrequest

            return enrollmentrequest.EnrollmentRequest(jsondict, strict)
        if "EnrollmentResponse" == resource_name:
            from . import enrollmentresponse

            return enrollmentresponse.EnrollmentResponse(jsondict, strict)
        if "EpisodeOfCare" == resource_name:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCare(jsondict, strict)
        if "EpisodeOfCareCareTeam" == resource_name:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCareCareTeam(jsondict, strict)
        if "EpisodeOfCareStatusHistory" == resource_name:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCareStatusHistory(jsondict, strict)
        if "ExplanationOfBenefit" == resource_name:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefit(jsondict, strict)
        if "Extension" == resource_name:
            from . import extension

            return extension.Extension(jsondict, strict)
        if "FamilyMemberHistory" == resource_name:
            from . import familymemberhistory

            return familymemberhistory.FamilyMemberHistory(jsondict, strict)
        if "FamilyMemberHistoryCondition" == resource_name:
            from . import familymemberhistory

            return familymemberhistory.FamilyMemberHistoryCondition(jsondict, strict)
        if "Flag" == resource_name:
            from . import flag

            return flag.Flag(jsondict, strict)
        if "Goal" == resource_name:
            from . import goal

            return goal.Goal(jsondict, strict)
        if "GoalOutcome" == resource_name:
            from . import goal

            return goal.GoalOutcome(jsondict, strict)
        if "Group" == resource_name:
            from . import group

            return group.Group(jsondict, strict)
        if "GroupCharacteristic" == resource_name:
            from . import group

            return group.GroupCharacteristic(jsondict, strict)
        if "GroupMember" == resource_name:
            from . import group

            return group.GroupMember(jsondict, strict)
        if "HealthcareService" == resource_name:
            from . import healthcareservice

            return healthcareservice.HealthcareService(jsondict, strict)
        if "HealthcareServiceAvailableTime" == resource_name:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceAvailableTime(jsondict, strict)
        if "HealthcareServiceNotAvailable" == resource_name:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceNotAvailable(jsondict, strict)
        if "HealthcareServiceServiceType" == resource_name:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceServiceType(jsondict, strict)
        if "HumanName" == resource_name:
            from . import humanname

            return humanname.HumanName(jsondict, strict)
        if "Identifier" == resource_name:
            from . import identifier

            return identifier.Identifier(jsondict, strict)
        if "ImagingObjectSelection" == resource_name:
            from . import imagingobjectselection

            return imagingobjectselection.ImagingObjectSelection(jsondict, strict)
        if "ImagingObjectSelectionStudy" == resource_name:
            from . import imagingobjectselection

            return imagingobjectselection.ImagingObjectSelectionStudy(jsondict, strict)
        if "ImagingObjectSelectionStudySeries" == resource_name:
            from . import imagingobjectselection

            return imagingobjectselection.ImagingObjectSelectionStudySeries(
                jsondict, strict
            )
        if "ImagingObjectSelectionStudySeriesInstance" == resource_name:
            from . import imagingobjectselection

            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstance(
                jsondict, strict
            )
        if "ImagingObjectSelectionStudySeriesInstanceFrames" == resource_name:
            from . import imagingobjectselection

            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstanceFrames(
                jsondict, strict
            )
        if "ImagingStudy" == resource_name:
            from . import imagingstudy

            return imagingstudy.ImagingStudy(jsondict, strict)
        if "ImagingStudySeries" == resource_name:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeries(jsondict, strict)
        if "ImagingStudySeriesInstance" == resource_name:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeriesInstance(jsondict, strict)
        if "Immunization" == resource_name:
            from . import immunization

            return immunization.Immunization(jsondict, strict)
        if "ImmunizationExplanation" == resource_name:
            from . import immunization

            return immunization.ImmunizationExplanation(jsondict, strict)
        if "ImmunizationReaction" == resource_name:
            from . import immunization

            return immunization.ImmunizationReaction(jsondict, strict)
        if "ImmunizationRecommendation" == resource_name:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendation(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendation" == resource_name:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendation(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_name:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendationProtocol" == resource_name:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol(
                jsondict, strict
            )
        if "ImmunizationVaccinationProtocol" == resource_name:
            from . import immunization

            return immunization.ImmunizationVaccinationProtocol(jsondict, strict)
        if "ImplementationGuide" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuide(jsondict, strict)
        if "ImplementationGuideContact" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuideContact(jsondict, strict)
        if "ImplementationGuideDependency" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuideDependency(jsondict, strict)
        if "ImplementationGuideGlobal" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuideGlobal(jsondict, strict)
        if "ImplementationGuidePackage" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuidePackage(jsondict, strict)
        if "ImplementationGuidePackageResource" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuidePackageResource(
                jsondict, strict
            )
        if "ImplementationGuidePage" == resource_name:
            from . import implementationguide

            return implementationguide.ImplementationGuidePage(jsondict, strict)
        if "List" == resource_name:
            from . import list

            return list.List(jsondict, strict)
        if "ListEntry" == resource_name:
            from . import list

            return list.ListEntry(jsondict, strict)
        if "Location" == resource_name:
            from . import location

            return location.Location(jsondict, strict)
        if "LocationPosition" == resource_name:
            from . import location

            return location.LocationPosition(jsondict, strict)
        if "Media" == resource_name:
            from . import media

            return media.Media(jsondict, strict)
        if "Medication" == resource_name:
            from . import medication

            return medication.Medication(jsondict, strict)
        if "MedicationAdministration" == resource_name:
            from . import medicationadministration

            return medicationadministration.MedicationAdministration(jsondict, strict)
        if "MedicationAdministrationDosage" == resource_name:
            from . import medicationadministration

            return medicationadministration.MedicationAdministrationDosage(
                jsondict, strict
            )
        if "MedicationDispense" == resource_name:
            from . import medicationdispense

            return medicationdispense.MedicationDispense(jsondict, strict)
        if "MedicationDispenseDosageInstruction" == resource_name:
            from . import medicationdispense

            return medicationdispense.MedicationDispenseDosageInstruction(
                jsondict, strict
            )
        if "MedicationDispenseSubstitution" == resource_name:
            from . import medicationdispense

            return medicationdispense.MedicationDispenseSubstitution(jsondict, strict)
        if "MedicationOrder" == resource_name:
            from . import medicationorder

            return medicationorder.MedicationOrder(jsondict, strict)
        if "MedicationOrderDispenseRequest" == resource_name:
            from . import medicationorder

            return medicationorder.MedicationOrderDispenseRequest(jsondict, strict)
        if "MedicationOrderDosageInstruction" == resource_name:
            from . import medicationorder

            return medicationorder.MedicationOrderDosageInstruction(jsondict, strict)
        if "MedicationOrderSubstitution" == resource_name:
            from . import medicationorder

            return medicationorder.MedicationOrderSubstitution(jsondict, strict)
        if "MedicationPackage" == resource_name:
            from . import medication

            return medication.MedicationPackage(jsondict, strict)
        if "MedicationPackageContent" == resource_name:
            from . import medication

            return medication.MedicationPackageContent(jsondict, strict)
        if "MedicationProduct" == resource_name:
            from . import medication

            return medication.MedicationProduct(jsondict, strict)
        if "MedicationProductBatch" == resource_name:
            from . import medication

            return medication.MedicationProductBatch(jsondict, strict)
        if "MedicationProductIngredient" == resource_name:
            from . import medication

            return medication.MedicationProductIngredient(jsondict, strict)
        if "MedicationStatement" == resource_name:
            from . import medicationstatement

            return medicationstatement.MedicationStatement(jsondict, strict)
        if "MedicationStatementDosage" == resource_name:
            from . import medicationstatement

            return medicationstatement.MedicationStatementDosage(jsondict, strict)
        if "MessageHeader" == resource_name:
            from . import messageheader

            return messageheader.MessageHeader(jsondict, strict)
        if "MessageHeaderDestination" == resource_name:
            from . import messageheader

            return messageheader.MessageHeaderDestination(jsondict, strict)
        if "MessageHeaderResponse" == resource_name:
            from . import messageheader

            return messageheader.MessageHeaderResponse(jsondict, strict)
        if "MessageHeaderSource" == resource_name:
            from . import messageheader

            return messageheader.MessageHeaderSource(jsondict, strict)
        if "Meta" == resource_name:
            from . import meta

            return meta.Meta(jsondict, strict)
        if "Money" == resource_name:
            from . import money

            return money.Money(jsondict, strict)
        if "NamingSystem" == resource_name:
            from . import namingsystem

            return namingsystem.NamingSystem(jsondict, strict)
        if "NamingSystemContact" == resource_name:
            from . import namingsystem

            return namingsystem.NamingSystemContact(jsondict, strict)
        if "NamingSystemUniqueId" == resource_name:
            from . import namingsystem

            return namingsystem.NamingSystemUniqueId(jsondict, strict)
        if "Narrative" == resource_name:
            from . import narrative

            return narrative.Narrative(jsondict, strict)
        if "NutritionOrder" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrder(jsondict, strict)
        if "NutritionOrderEnteralFormula" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrderEnteralFormula(jsondict, strict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrderEnteralFormulaAdministration(
                jsondict, strict
            )
        if "NutritionOrderOralDiet" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDiet(jsondict, strict)
        if "NutritionOrderOralDietNutrient" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDietNutrient(jsondict, strict)
        if "NutritionOrderOralDietTexture" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDietTexture(jsondict, strict)
        if "NutritionOrderSupplement" == resource_name:
            from . import nutritionorder

            return nutritionorder.NutritionOrderSupplement(jsondict, strict)
        if "Observation" == resource_name:
            from . import observation

            return observation.Observation(jsondict, strict)
        if "ObservationComponent" == resource_name:
            from . import observation

            return observation.ObservationComponent(jsondict, strict)
        if "ObservationReferenceRange" == resource_name:
            from . import observation

            return observation.ObservationReferenceRange(jsondict, strict)
        if "ObservationRelated" == resource_name:
            from . import observation

            return observation.ObservationRelated(jsondict, strict)
        if "OperationDefinition" == resource_name:
            from . import operationdefinition

            return operationdefinition.OperationDefinition(jsondict, strict)
        if "OperationDefinitionContact" == resource_name:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionContact(jsondict, strict)
        if "OperationDefinitionParameter" == resource_name:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameter(jsondict, strict)
        if "OperationDefinitionParameterBinding" == resource_name:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameterBinding(
                jsondict, strict
            )
        if "OperationOutcome" == resource_name:
            from . import operationoutcome

            return operationoutcome.OperationOutcome(jsondict, strict)
        if "OperationOutcomeIssue" == resource_name:
            from . import operationoutcome

            return operationoutcome.OperationOutcomeIssue(jsondict, strict)
        if "Order" == resource_name:
            from . import order

            return order.Order(jsondict, strict)
        if "OrderResponse" == resource_name:
            from . import orderresponse

            return orderresponse.OrderResponse(jsondict, strict)
        if "OrderWhen" == resource_name:
            from . import order

            return order.OrderWhen(jsondict, strict)
        if "Organization" == resource_name:
            from . import organization

            return organization.Organization(jsondict, strict)
        if "OrganizationContact" == resource_name:
            from . import organization

            return organization.OrganizationContact(jsondict, strict)
        if "Parameters" == resource_name:
            from . import parameters

            return parameters.Parameters(jsondict, strict)
        if "ParametersParameter" == resource_name:
            from . import parameters

            return parameters.ParametersParameter(jsondict, strict)
        if "Patient" == resource_name:
            from . import patient

            return patient.Patient(jsondict, strict)
        if "PatientAnimal" == resource_name:
            from . import patient

            return patient.PatientAnimal(jsondict, strict)
        if "PatientCommunication" == resource_name:
            from . import patient

            return patient.PatientCommunication(jsondict, strict)
        if "PatientContact" == resource_name:
            from . import patient

            return patient.PatientContact(jsondict, strict)
        if "PatientLink" == resource_name:
            from . import patient

            return patient.PatientLink(jsondict, strict)
        if "PaymentNotice" == resource_name:
            from . import paymentnotice

            return paymentnotice.PaymentNotice(jsondict, strict)
        if "PaymentReconciliation" == resource_name:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliation(jsondict, strict)
        if "PaymentReconciliationDetail" == resource_name:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliationDetail(jsondict, strict)
        if "PaymentReconciliationNote" == resource_name:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliationNote(jsondict, strict)
        if "Period" == resource_name:
            from . import period

            return period.Period(jsondict, strict)
        if "Person" == resource_name:
            from . import person

            return person.Person(jsondict, strict)
        if "PersonLink" == resource_name:
            from . import person

            return person.PersonLink(jsondict, strict)
        if "Practitioner" == resource_name:
            from . import practitioner

            return practitioner.Practitioner(jsondict, strict)
        if "PractitionerPractitionerRole" == resource_name:
            from . import practitioner

            return practitioner.PractitionerPractitionerRole(jsondict, strict)
        if "PractitionerQualification" == resource_name:
            from . import practitioner

            return practitioner.PractitionerQualification(jsondict, strict)
        if "Procedure" == resource_name:
            from . import procedure

            return procedure.Procedure(jsondict, strict)
        if "ProcedureFocalDevice" == resource_name:
            from . import procedure

            return procedure.ProcedureFocalDevice(jsondict, strict)
        if "ProcedurePerformer" == resource_name:
            from . import procedure

            return procedure.ProcedurePerformer(jsondict, strict)
        if "ProcedureRequest" == resource_name:
            from . import procedurerequest

            return procedurerequest.ProcedureRequest(jsondict, strict)
        if "ProcessRequest" == resource_name:
            from . import processrequest

            return processrequest.ProcessRequest(jsondict, strict)
        if "ProcessRequestItem" == resource_name:
            from . import processrequest

            return processrequest.ProcessRequestItem(jsondict, strict)
        if "ProcessResponse" == resource_name:
            from . import processresponse

            return processresponse.ProcessResponse(jsondict, strict)
        if "ProcessResponseNotes" == resource_name:
            from . import processresponse

            return processresponse.ProcessResponseNotes(jsondict, strict)
        if "Provenance" == resource_name:
            from . import provenance

            return provenance.Provenance(jsondict, strict)
        if "ProvenanceAgent" == resource_name:
            from . import provenance

            return provenance.ProvenanceAgent(jsondict, strict)
        if "ProvenanceAgentRelatedAgent" == resource_name:
            from . import provenance

            return provenance.ProvenanceAgentRelatedAgent(jsondict, strict)
        if "ProvenanceEntity" == resource_name:
            from . import provenance

            return provenance.ProvenanceEntity(jsondict, strict)
        if "Quantity" == resource_name:
            from . import quantity

            return quantity.Quantity(jsondict, strict)
        if "Questionnaire" == resource_name:
            from . import questionnaire

            return questionnaire.Questionnaire(jsondict, strict)
        if "QuestionnaireGroup" == resource_name:
            from . import questionnaire

            return questionnaire.QuestionnaireGroup(jsondict, strict)
        if "QuestionnaireGroupQuestion" == resource_name:
            from . import questionnaire

            return questionnaire.QuestionnaireGroupQuestion(jsondict, strict)
        if "QuestionnaireResponse" == resource_name:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponse(jsondict, strict)
        if "QuestionnaireResponseGroup" == resource_name:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseGroup(jsondict, strict)
        if "QuestionnaireResponseGroupQuestion" == resource_name:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseGroupQuestion(
                jsondict, strict
            )
        if "QuestionnaireResponseGroupQuestionAnswer" == resource_name:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseGroupQuestionAnswer(
                jsondict, strict
            )
        if "Range" == resource_name:
            from . import range

            return range.Range(jsondict, strict)
        if "Ratio" == resource_name:
            from . import ratio

            return ratio.Ratio(jsondict, strict)
        if "Reference" == resource_name:
            from . import reference

            return reference.Reference(jsondict, strict)
        if "ReferralRequest" == resource_name:
            from . import referralrequest

            return referralrequest.ReferralRequest(jsondict, strict)
        if "RelatedPerson" == resource_name:
            from . import relatedperson

            return relatedperson.RelatedPerson(jsondict, strict)
        if "Resource" == resource_name:
            from . import resource

            return resource.Resource(jsondict, strict)
        if "RiskAssessment" == resource_name:
            from . import riskassessment

            return riskassessment.RiskAssessment(jsondict, strict)
        if "RiskAssessmentPrediction" == resource_name:
            from . import riskassessment

            return riskassessment.RiskAssessmentPrediction(jsondict, strict)
        if "SampledData" == resource_name:
            from . import sampleddata

            return sampleddata.SampledData(jsondict, strict)
        if "Schedule" == resource_name:
            from . import schedule

            return schedule.Schedule(jsondict, strict)
        if "SearchParameter" == resource_name:
            from . import searchparameter

            return searchparameter.SearchParameter(jsondict, strict)
        if "SearchParameterContact" == resource_name:
            from . import searchparameter

            return searchparameter.SearchParameterContact(jsondict, strict)
        if "Signature" == resource_name:
            from . import signature

            return signature.Signature(jsondict, strict)
        if "Slot" == resource_name:
            from . import slot

            return slot.Slot(jsondict, strict)
        if "Specimen" == resource_name:
            from . import specimen

            return specimen.Specimen(jsondict, strict)
        if "SpecimenCollection" == resource_name:
            from . import specimen

            return specimen.SpecimenCollection(jsondict, strict)
        if "SpecimenContainer" == resource_name:
            from . import specimen

            return specimen.SpecimenContainer(jsondict, strict)
        if "SpecimenTreatment" == resource_name:
            from . import specimen

            return specimen.SpecimenTreatment(jsondict, strict)
        if "StructureDefinition" == resource_name:
            from . import structuredefinition

            return structuredefinition.StructureDefinition(jsondict, strict)
        if "StructureDefinitionContact" == resource_name:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionContact(jsondict, strict)
        if "StructureDefinitionDifferential" == resource_name:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionDifferential(jsondict, strict)
        if "StructureDefinitionMapping" == resource_name:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionMapping(jsondict, strict)
        if "StructureDefinitionSnapshot" == resource_name:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionSnapshot(jsondict, strict)
        if "Subscription" == resource_name:
            from . import subscription

            return subscription.Subscription(jsondict, strict)
        if "SubscriptionChannel" == resource_name:
            from . import subscription

            return subscription.SubscriptionChannel(jsondict, strict)
        if "Substance" == resource_name:
            from . import substance

            return substance.Substance(jsondict, strict)
        if "SubstanceIngredient" == resource_name:
            from . import substance

            return substance.SubstanceIngredient(jsondict, strict)
        if "SubstanceInstance" == resource_name:
            from . import substance

            return substance.SubstanceInstance(jsondict, strict)
        if "SupplyDelivery" == resource_name:
            from . import supplydelivery

            return supplydelivery.SupplyDelivery(jsondict, strict)
        if "SupplyRequest" == resource_name:
            from . import supplyrequest

            return supplyrequest.SupplyRequest(jsondict, strict)
        if "SupplyRequestWhen" == resource_name:
            from . import supplyrequest

            return supplyrequest.SupplyRequestWhen(jsondict, strict)
        if "TestScript" == resource_name:
            from . import testscript

            return testscript.TestScript(jsondict, strict)
        if "TestScriptContact" == resource_name:
            from . import testscript

            return testscript.TestScriptContact(jsondict, strict)
        if "TestScriptFixture" == resource_name:
            from . import testscript

            return testscript.TestScriptFixture(jsondict, strict)
        if "TestScriptMetadata" == resource_name:
            from . import testscript

            return testscript.TestScriptMetadata(jsondict, strict)
        if "TestScriptMetadataCapability" == resource_name:
            from . import testscript

            return testscript.TestScriptMetadataCapability(jsondict, strict)
        if "TestScriptMetadataLink" == resource_name:
            from . import testscript

            return testscript.TestScriptMetadataLink(jsondict, strict)
        if "TestScriptSetup" == resource_name:
            from . import testscript

            return testscript.TestScriptSetup(jsondict, strict)
        if "TestScriptSetupAction" == resource_name:
            from . import testscript

            return testscript.TestScriptSetupAction(jsondict, strict)
        if "TestScriptSetupActionAssert" == resource_name:
            from . import testscript

            return testscript.TestScriptSetupActionAssert(jsondict, strict)
        if "TestScriptSetupActionOperation" == resource_name:
            from . import testscript

            return testscript.TestScriptSetupActionOperation(jsondict, strict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_name:
            from . import testscript

            return testscript.TestScriptSetupActionOperationRequestHeader(
                jsondict, strict
            )
        if "TestScriptTeardown" == resource_name:
            from . import testscript

            return testscript.TestScriptTeardown(jsondict, strict)
        if "TestScriptTeardownAction" == resource_name:
            from . import testscript

            return testscript.TestScriptTeardownAction(jsondict, strict)
        if "TestScriptTest" == resource_name:
            from . import testscript

            return testscript.TestScriptTest(jsondict, strict)
        if "TestScriptTestAction" == resource_name:
            from . import testscript

            return testscript.TestScriptTestAction(jsondict, strict)
        if "TestScriptVariable" == resource_name:
            from . import testscript

            return testscript.TestScriptVariable(jsondict, strict)
        if "Timing" == resource_name:
            from . import timing

            return timing.Timing(jsondict, strict)
        if "TimingRepeat" == resource_name:
            from . import timing

            return timing.TimingRepeat(jsondict, strict)
        if "ValueSet" == resource_name:
            from . import valueset

            return valueset.ValueSet(jsondict, strict)
        if "ValueSetCodeSystem" == resource_name:
            from . import valueset

            return valueset.ValueSetCodeSystem(jsondict, strict)
        if "ValueSetCodeSystemConcept" == resource_name:
            from . import valueset

            return valueset.ValueSetCodeSystemConcept(jsondict, strict)
        if "ValueSetCodeSystemConceptDesignation" == resource_name:
            from . import valueset

            return valueset.ValueSetCodeSystemConceptDesignation(jsondict, strict)
        if "ValueSetCompose" == resource_name:
            from . import valueset

            return valueset.ValueSetCompose(jsondict, strict)
        if "ValueSetComposeInclude" == resource_name:
            from . import valueset

            return valueset.ValueSetComposeInclude(jsondict, strict)
        if "ValueSetComposeIncludeConcept" == resource_name:
            from . import valueset

            return valueset.ValueSetComposeIncludeConcept(jsondict, strict)
        if "ValueSetComposeIncludeFilter" == resource_name:
            from . import valueset

            return valueset.ValueSetComposeIncludeFilter(jsondict, strict)
        if "ValueSetContact" == resource_name:
            from . import valueset

            return valueset.ValueSetContact(jsondict, strict)
        if "ValueSetExpansion" == resource_name:
            from . import valueset

            return valueset.ValueSetExpansion(jsondict, strict)
        if "ValueSetExpansionContains" == resource_name:
            from . import valueset

            return valueset.ValueSetExpansionContains(jsondict, strict)
        if "ValueSetExpansionParameter" == resource_name:
            from . import valueset

            return valueset.ValueSetExpansionParameter(jsondict, strict)
        if "VisionPrescription" == resource_name:
            from . import visionprescription

            return visionprescription.VisionPrescription(jsondict, strict)
        if "VisionPrescriptionDispense" == resource_name:
            from . import visionprescription

            return visionprescription.VisionPrescriptionDispense(jsondict, strict)
        from . import element

        return element.Element(jsondict, strict)
