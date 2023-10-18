import xml.etree.ElementTree as ET

data_dict = dict_2 = dict_3 = {
  'root/root/check/MessageHeaderDocument/ram:ID': 'f17ec2f9-a67d-4785-9a42-272edc272269',
  'root/root/check/MessageHeaderDocument/ram:Name': 'Air Waybill',
  'root/root/check/MessageHeaderDocument/ram:TypeCode (attribute_name)-listID': '1001',
  'root/root/check/MessageHeaderDocument/ram:TypeCode (attribute_name)-listVersionID': 'D09A',
  'root/root/check/MessageHeaderDocument/ram:TypeCode': '741',
  'root/root/check/MessageHeaderDocument/ram:IssueDateTime': '2022-11-11T10:32:30',
  'root/root/check/MessageHeaderDocument/ram:PurposeCode': 'Creation',
  'root/root/check/MessageHeaderDocument/ram:VersionID': '3',
  'root/root/check/MessageHeaderDocument/ram:ConversationID': 'dbb22bf1-840a-47e2-9409-51b620c20973',
  'root/root/check/MessageHeaderDocument/ram:SenderParty/ram:PrimaryID (attribute_name)-schemeID': 'P',
  'root/root/check/MessageHeaderDocument/ram:SenderParty/ram:PrimaryID': 'CSGAIR01DXBFMEK',
  'root/root/check/MessageHeaderDocument/ram:RecipientParty/ram:PrimaryID (attribute_name)-schemeID': 'P',
  'root/root/check/MessageHeaderDocument/ram:RecipientParty/ram:PrimaryID': 'CSGCUS86CUSGW',
  'root/root/check/BusinessHeaderDocument/ram:ID': '176-01112228',
  'root/root/check/BusinessHeaderDocument/ram:SignatoryCarrierAuthentication/ram:ActualDateTime': '2021-12-10T00:00:00',
  'root/root/check/BusinessHeaderDocument/ram:SignatoryCarrierAuthentication/ram:Signatory': 'DHL EXPRESS',
  'root/root/check/BusinessHeaderDocument/ram:SignatoryCarrierAuthentication/ram:IssueAuthenticationLocation/ram:Name': 'SINGAPORE',
  'root/root/check/MasterConsignment/ram:NilCarriageValueIndicator': 'true',
  'root/root/check/MasterConsignment/ram:NilCustomsValueIndicator': 'true',
  'root/root/check/MasterConsignment/ram:DeclaredValueForCustomsAmount (attribute_name)-currencyID': 'TWD',
  'root/root/check/MasterConsignment/ram:DeclaredValueForCustomsAmount': '0',
  'root/root/check/MasterConsignment/ram:NilInsuranceValueIndicator': 'true',
  'root/root/check/MasterConsignment/ram:InsuranceValueAmount (attribute_name)-currencyID': 'TWD',
  'root/root/check/MasterConsignment/ram:InsuranceValueAmount': '0',
  'root/root/check/MasterConsignment/ram:TotalChargePrepaidIndicator': 'true',
  'root/root/check/MasterConsignment/ram:TotalDisbursementPrepaidIndicator': 'true',
  'root/root/check/MasterConsignment/ram:IncludedTareGrossWeightMeasure (attribute_name)-unitCode': 'KGM',
  'root/root/check/MasterConsignment/ram:IncludedTareGrossWeightMeasure': '24',
  'root/root/check/MasterConsignment/ram:GrossVolumeMeasure (attribute_name)-unitCode': 'MTQ',
  'root/root/check/MasterConsignment/ram:GrossVolumeMeasure': '32',
  'root/root/check/MasterConsignment/ram:TotalPieceQuantity': '5',
  'root/root/check/MasterConsignment/ram:ConsignorParty/ram:Name': 'SENSESOFT 002',
  'root/root/check/MasterConsignment/ram:ConsignorParty/ram:PostalStructuredAddress/ram:StreetName': '1 BDOTTS RD.',
  'root/root/check/MasterConsignment/ram:ConsignorParty/ram:PostalStructuredAddress/ram:CityName': 'SINGAPORE',
  'root/root/check/MasterConsignment/ram:ConsignorParty/ram:PostalStructuredAddress/ram:CountryID (attribute_name)-schemeVersionID': 'second edition 2006',
  'root/root/check/MasterConsignment/ram:ConsignorParty/ram:PostalStructuredAddress/ram:CountryID': 'SG',
  'root/root/check/MasterConsignment/ram:ConsigneeParty/ram:Name': 'DHL EXPRESS',
  'root/root/check/MasterConsignment/ram:ConsigneeParty/ram:PostalStructuredAddress/ram:StreetName': '123 ST. LAGOS',
  'root/root/check/MasterConsignment/ram:ConsigneeParty/ram:PostalStructuredAddress/ram:CityName': 'BANGLADESH',
  'root/root/check/MasterConsignment/ram:ConsigneeParty/ram:PostalStructuredAddress/ram:CountryID (attribute_name)-schemeVersionID': 'second edition 2006',
  'root/root/check/MasterConsignment/ram:ConsigneeParty/ram:PostalStructuredAddress/ram:CountryID': 'BR',
  'root/root/check/MasterConsignment/ram:FreightForwarderParty/ram:Name': 'DHL EXPRESS',
  'root/root/check/MasterConsignment/ram:FreightForwarderParty/ram:CargoAgentID': '1234567',
  'root/root/check/MasterConsignment/ram:FreightForwarderParty/ram:FreightForwarderAddress/ram:CityName': 'SINGAPORE',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:Name': 'DHL EXPRESS',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:RoleCode (attribute_name)-listID': '3035',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:RoleCode (attribute_name)-listVersionID': 'D09A',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:RoleCode': 'NI',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:PostalStructuredAddress/ram:StreetName': '123 ST. LAGOS',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:PostalStructuredAddress/ram:CityName': 'BANGLADESH',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:PostalStructuredAddress/ram:CountryID (attribute_name)-schemeVersionID': 'second edition 2006',
  'root/root/check/MasterConsignment/ram:AssociatedParty/ram:PostalStructuredAddress/ram:CountryID': 'BR',
  'root/root/check/MasterConsignment/ram:OriginLocation/ram:ID': 'SIN',
  'root/root/check/MasterConsignment/ram:FinalDestinationLocation/ram:ID': 'DAC',
  'root/root/check/MasterConsignment/ram:SpecifiedLogisticsTransportMovement/ram:ID': 'EK0111',
  'root/root/check/MasterConsignment/ram:SpecifiedLogisticsTransportMovement/ram:UsedLogisticsTransportMeans/ram:Name': 'EK',
  'root/root/check/MasterConsignment/ram:SpecifiedLogisticsTransportMovement/ram:ArrivalEvent/ram:ScheduledOccurrenceDateTime': '2021-12-05T00:00:00',
  'root/root/check/MasterConsignment/ram:SpecifiedLogisticsTransportMovement/ram:ArrivalEvent/ram:OccurrenceArrivalLocation/ram:ID': 'BKK',
  'root/root/check/MasterConsignment/ram:SpecifiedLogisticsTransportMovement/ram:ArrivalEvent/ram:OccurrenceArrivalLocation/ram:Name': 'QR',
  'root/root/check/MasterConsignment/ram:SpecifiedLogisticsTransportMovement/ram:DepartureEvent/ram:ScheduledOccurrenceDateTime': '2021-12-05T00:00:00',
  'root/root/check/MasterConsignment/ram:ApplicableOriginCurrencyExchange/ram:SourceCurrencyCode (attribute_name)-listID': 'ISO 4217 3A',
  'root/root/check/MasterConsignment/ram:ApplicableOriginCurrencyExchange/ram:SourceCurrencyCode (attribute_name)-listVersionID': '2007-06-18',
  'root/root/check/MasterConsignment/ram:ApplicableOriginCurrencyExchange/ram:SourceCurrencyCode': 'SGD',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:TypeCode': 'F',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:SequenceNumeric': '1',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:GrossWeightMeasure (attribute_name)-unitCode': 'KGM',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:GrossWeightMeasure': '5',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:PieceQuantity': '1',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:NatureIdentificationTransportCargo/ram:Identification': 'CONSOLLAPTOPS 12345 90416274 DELIVERY',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:ApplicableFreightRateServiceCharge/ram:CategoryCode': 'M',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:ApplicableFreightRateServiceCharge/ram:ChargeableWeightMeasure (attribute_name)-unitCode': 'KGM',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:ApplicableFreightRateServiceCharge/ram:ChargeableWeightMeasure': '3.523',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:ApplicableFreightRateServiceCharge/ram:AppliedRate': '5',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:ApplicableFreightRateServiceCharge/ram:AppliedAmount (attribute_name)-currencyID': 'SGD',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem/ram:ApplicableFreightRateServiceCharge/ram:AppliedAmount': '5',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem__duplicate__/ram:SequenceNumeric': '2',
  'root/root/check/MasterConsignment/ram:ApplicableRating/ram:IncludedMasterConsignmentItem__duplicate__/ram:Information': 'NDA',
  'root/root/check/MasterConsignment/ram:ApplicableTotalRating/ram:TypeCode': 'F',
  'root/root/check/MasterConsignment/ram:ApplicableTotalRating/ram:ApplicablePrepaidCollectMonetarySummation/ram:PrepaidIndicator': 'true',
  'root/root/check/MasterConsignment/ram:ApplicableTotalRating/ram:ApplicablePrepaidCollectMonetarySummation/ram:WeightChargeTotalAmount (attribute_name)-currencyID': 'SGD',
  'root/root/check/MasterConsignment/ram:ApplicableTotalRating/ram:ApplicablePrepaidCollectMonetarySummation/ram:WeightChargeTotalAmount': '800',
  'root/root/check/MasterConsignment/ram:ApplicableTotalRating/ram:ApplicablePrepaidCollectMonetarySummation/ram:GrandTotalAmount (attribute_name)-currencyID': 'SGD',
  'root/root/check/MasterConsignment/ram:ApplicableTotalRating/ram:ApplicablePrepaidCollectMonetarySummation/ram:GrandTotalAmount': '800'
}

def dict_to_xml(d):
    root = ET.Element("root")
    for key, value in d.items():
        elements = key.split('/')
        current = root
        previous_element = 0
        for element in elements:
            if "(attribute_name)" in element:
                # continue
                pair = element.split(" (attribute_name)-")
                attr_name = pair[1]
                element = pair[0]
                if element not in [child.tag for child in current]:
                    child = ET.SubElement(current, element)
                    child.set(attr_name, value)
                elif element in [child.tag for child in current]:
                    child.set(attr_name, value)
                current = [child for child in current if child.tag == element][0]
            else:
                if element not in [child.tag for child in current]:
                    child = ET.SubElement(current, element)
                current = [child for child in current if child.tag == element][0]
        if value and "(attribute_name)" not in key:
            current.text = value
    return ET.tostring(root).decode()


xml_data = dict_to_xml(data_dict)
print(xml_data)

