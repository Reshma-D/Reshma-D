//$Id$
package com.zoho.zia.crm.feature.barcodeReader;

import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;

import com.adventnet.iam.security.UploadedFileItem;
import com.google.gson.JsonObject;
import com.google.zxing.BinaryBitmap;
import com.google.zxing.LuminanceSource;
import com.google.zxing.client.j2se.BufferedImageLuminanceSource;
import com.google.zxing.common.HybridBinarizer;
import com.zoho.zia.crm.feature.barcodeReader.BarcodeInformation;

public class ReadBarcodeQRProcessor {
	
public static String scanBarcode(File fileStream, String barcode_format) {
		
		try {
			//Reading image file 
			BufferedImage barCodeBufferedImage = ImageIO.read(fileStream);
			
			//LuminanceSource Implementation is meant for J2SE clients 
		    LuminanceSource source = new BufferedImageLuminanceSource(barCodeBufferedImage);
		    
		    //To represent 1 bit data
		    BinaryBitmap bitmap = new BinaryBitmap(new HybridBinarizer(source));
		    
		    String barcode_info = BarcodeInformation.getBarcodeInfo(bitmap, barcode_format);
		    JsonObject res_json = new JsonObject();
		    if (barcode_info.equals("null")) {
		    		res_json.addProperty("status", "success"); //No I18N
//				res_json.addProperty("code", "NO_BARCODE_DETECTED"); //No I18N
//				res_json.addProperty("message", "no barcode information detected"); //No I18N
//				res_json.addProperty("details", "{}"); //No I18N
				JsonObject response = new JsonObject();
				response.addProperty("content", ""); //No I18N
				res_json.add("response", response); //No I18N
				return res_json.toString(); 	    		
		    } else {
		    		res_json.addProperty("status", "success"); //No I18N
//				res_json.addProperty("code", "BARCODE_DETECTED"); //No I18N
//				res_json.addProperty("message", "barcode information detected"); //No I18N
//				res_json.addProperty("details", "{}"); //No I18N
				JsonObject response = new JsonObject();
				response.addProperty("content", barcode_info); //No I18N
				res_json.add("response", response); //No I18N
				return res_json.toString(); 	    	
		    }
			
		}
		catch (Exception e) {
			return e.toString();
		}
	}

}
