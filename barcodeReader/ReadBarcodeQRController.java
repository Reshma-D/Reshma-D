//$Id$
package com.zoho.zia.crm.feature.barcodeReader;

import java.io.File;
import java.util.ArrayList;
import java.util.logging.Logger;

import javax.servlet.http.HttpServletRequest;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.adventnet.iam.security.SecurityUtil;
import com.adventnet.iam.security.UploadedFileItem;
import com.google.gson.JsonObject;
import com.zoho.zia.crm.feature.barcodeReader.ReadBarcodeQRProcessor;
import com.zoho.zia.crm.feature.barcodeReader.ImageVerification;

@RestController
@RequestMapping("/crm/zia/image/barcode/v1")  //No I18N
public class ReadBarcodeQRController {
	
	public static final Logger LOGGER = Logger.getLogger("Barcode Scanner");
	public static JsonObject res_json = new JsonObject();
	
	@RequestMapping(value = "/describe", method = RequestMethod.GET, produces = {MediaType.APPLICATION_JSON_VALUE})   //No I18N
	public static ResponseEntity<String> describe_feature() {
		
		try {
			return new ResponseEntity<String>(FeatureDescription.describeFeature(),HttpStatus.OK);
		}
		catch(Exception e) {
			LOGGER.info(e.toString());
			res_json.addProperty("status", "error"); //No I18N
			res_json.addProperty("code", "UNKNOWN_ERROR"); //No I18N
			res_json.addProperty("message", ""); //No I18N
			res_json.addProperty("details", "{}"); //No I18N
//			res_json.addProperty("response", "error occured while processing your request"); //No I18N
			return new ResponseEntity("" + res_json.toString() + "",HttpStatus.BAD_REQUEST);  //No I18N
		}
	}
	

	@RequestMapping(value = "/predict", method = RequestMethod.POST, produces = {MediaType.APPLICATION_JSON_VALUE})   //No I18N
	public static ResponseEntity<String> scanBarcode(HttpServletRequest request, @RequestParam String format) {
		
		LOGGER.info("In barcode scanning");
		long start = System.currentTimeMillis();
				
		try {
			//Reading the file uploaded
			Object uploaded_file = request.getAttribute(SecurityUtil.MULTIPART_FORM_REQUEST); 
			ArrayList file_list = new ArrayList();
			file_list = (ArrayList)uploaded_file;	
			File imageFile = ((UploadedFileItem) file_list.get(0)).getUploadedFile();	
			
			//Image verification and initialising barcode scanning
			String verification = ImageVerification.verifyImageFormat(format, file_list);
			if(verification.equals("true")) {
				String res_json= ReadBarcodeQRProcessor.scanBarcode(imageFile, format);
				LOGGER.info("Time taken: " + Float.toString(((System.currentTimeMillis() - start)/1000F)) + "seconds");
				return new ResponseEntity<String>(""+ res_json + "", HttpStatus.OK);	
			} else {
				LOGGER.info("Time taken: " + Float.toString(((System.currentTimeMillis() - start)/1000F)) + "seconds");
				return new ResponseEntity(""+ verification + "",HttpStatus.BAD_REQUEST);  //No I18N
			}
		}
		catch(Exception e) {
			LOGGER.info(e.toString());
			res_json.addProperty("status", "error"); //No I18N
			res_json.addProperty("code", "UNKNOWN_ERROR"); //No I18N
			res_json.addProperty("message", ""); //No I18N
			res_json.addProperty("details", "{}"); //No I18N
//			res_json.addProperty("response", "error occured while processing your request"); //No I18N
			return new ResponseEntity("" + res_json.toString() + "",HttpStatus.BAD_REQUEST);  //No I18N
		}
		
	}
}
