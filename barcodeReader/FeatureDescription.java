//$Id$
package com.zoho.zia.crm.feature.barcodeReader;

import com.google.gson.JsonObject;

public class FeatureDescription {
	
	public static String describeFeature() {
		JsonObject describe = new JsonObject();
		describe.addProperty("prediction", "predicts barcode and qrcode information in an image");//No I18N

		JsonObject barcode_format = new JsonObject();
		barcode_format.addProperty("1.","code39");	//No I18N
		barcode_format.addProperty("2.","code128");	//No I18N
		barcode_format.addProperty("3.","code93");	//No I18N
		barcode_format.addProperty("4.","ean8");		//No I18N
		barcode_format.addProperty("5.","ean13");	//No I18N
		barcode_format.addProperty("6.","codabar");	//No I18N
		barcode_format.addProperty("7.","itf");		//No I18N
		barcode_format.addProperty("8.","upca");		//No I18N
		barcode_format.addProperty("9.","upce");		//No I18N
		barcode_format.addProperty("10.","datamatrix");//No I18N
		barcode_format.addProperty("11.","aztec");//No I18N
		barcode_format.addProperty("12.","pdf417");//No I18N
		barcode_format.addProperty("13.","rss");//No I18N
		barcode_format.addProperty("14.","qrcode");//No I18N
		
		describe.add("supported_barcode_format", barcode_format);//No I18N
		describe.addProperty("accepted_image_type", ".jpg, .jpeg and .png");//No I18N
		return (describe.toString());
	}

}
