//$Id$
package com.zoho.zia.crm.feature.barcodeReader;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.adventnet.iam.security.UploadedFileItem;
import com.google.gson.JsonObject;
import com.zoho.zia.crm.feature.barcodeReader.Constant;

public class ImageVerification {
	
	public static boolean verifyBarcodeFormat(String barcode_format) {
		List<String> barcode_format_list = Arrays.asList(Constant.BARCODEFORMATS);
		return (barcode_format_list.contains(barcode_format) ? true : false); 
	}

	public static boolean verifyFileFormat(String fileName) {
		String extension[] = fileName.split("\\.");
		List<String> file_format_list = Arrays.asList(Constant.FILEFORMATS);
		return (file_format_list.contains(extension[extension.length - 1]) ? true : false);
	}
	
	public static boolean verifyFileSize(long fileSize) throws IOException {
		return (fileSize < Constant.MAXIMGSIZE ? true : false);
	}
	
	public static String verifyImageFormat(String barcode_format, ArrayList file_list) throws IOException {
		JsonObject res_json = new JsonObject();
		if(!(verifyBarcodeFormat(barcode_format))) { 
			res_json.addProperty("status", "failure"); //No I18N
			res_json.addProperty("code", "UNSUPPORTED_FORMAT_ERROR"); //No I18N
			res_json.addProperty("message", ""); //No I18N
			res_json.addProperty("details", "{}"); //No I18N
//			res_json.addProperty("response", "'"+ barcode_format +"' is not a supported barcode format"); //No I18N
		return res_json.toString(); 
		}
		if(!(verifyFileFormat(((UploadedFileItem) file_list.get(0)).getFileName()))) {
			res_json.addProperty("status", "failure"); //No I18N
			res_json.addProperty("code", "UNSUPPORTED_FORMAT_ERROR"); //No I18N
			res_json.addProperty("message", ""); //No I18N
			res_json.addProperty("details", "{}"); //No I18N
//			res_json.addProperty("response", "'"+ ((UploadedFileItem) file_list.get(0)).getFileName() +"' does not holds supported image format"); //No I18N
		return res_json.toString(); 
		}
		if(!(verifyFileSize(((UploadedFileItem) file_list.get(0)).getFileSize()))) {
			res_json.addProperty("status", "failure"); //No I18N
			res_json.addProperty("code", "MEMORY_EXCEEDS_ERROR"); //No I18N
			res_json.addProperty("message", ""); //No I18N
			res_json.addProperty("details", "{}"); //No I18N
//			res_json.addProperty("response", "uploaded image file exceeds the allocated memory limit"); //No I18N
		return res_json.toString(); 
		}
		
		return "true";
	}
}
