//$Id$
package com.zoho.zia.crm.feature.barcodeReader;

import java.util.Hashtable;
import java.util.logging.Logger;

import com.google.zxing.BinaryBitmap;
import com.google.zxing.DecodeHintType;
import com.google.zxing.MultiFormatReader;
import com.google.zxing.Result;
import com.google.zxing.aztec.AztecReader;
import com.google.zxing.datamatrix.DataMatrixReader;
import com.google.zxing.oned.CodaBarReader;
import com.google.zxing.oned.Code128Reader;
import com.google.zxing.oned.Code39Reader;
import com.google.zxing.oned.Code93Reader;
import com.google.zxing.oned.EAN13Reader;
import com.google.zxing.oned.EAN8Reader;
import com.google.zxing.oned.ITFReader;
import com.google.zxing.oned.UPCAReader;
import com.google.zxing.oned.UPCEReader;
import com.google.zxing.oned.rss.expanded.RSSExpandedReader;
import com.google.zxing.pdf417.PDF417Reader;
import com.google.zxing.qrcode.QRCodeReader;

public class BarcodeInformation {
	
	public static final Logger LOGGER = Logger.getLogger("Getting Barcode Content");
	
	public static String getBarcodeInfo(BinaryBitmap bitmap, String barcodeformat) {
		
		try {
			//Encapsulates a type of hint that a caller may pass to a barcode reader to help it more quickly or accurately decode it
		    Hashtable<DecodeHintType, Boolean> hints = new Hashtable<DecodeHintType, Boolean>();
		    hints.put(DecodeHintType.TRY_HARDER, Boolean.TRUE);
		    String BARCODE_FORMAT = barcodeformat;  
		    Result result = null;
		    if(BARCODE_FORMAT.equalsIgnoreCase("all")) {
		    	result = new MultiFormatReader().decode(bitmap, hints);
		    } 
		    else if(BARCODE_FORMAT.equalsIgnoreCase("qrcode")) {
		    	result = new QRCodeReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("code128")) {
		    	result = new Code128Reader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("code39")) {
		    	result = new Code39Reader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("code93")) {
		    	result = new Code93Reader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("ean13")) {
		    	result = new EAN13Reader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("ean8")) {
		    	result = new EAN8Reader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("codabar")) {
		    	result = new CodaBarReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("itf")) {
		    	result = new ITFReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("upca")) {
		    	result = new UPCAReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("upce")) {
		    	result = new UPCEReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("datamatrix")) {
		    	result = new DataMatrixReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("aztec")) {
		    	result = new AztecReader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("pdf417")) {
		    	result = new PDF417Reader().decode(bitmap, hints);
		    }
		    else if(BARCODE_FORMAT.equalsIgnoreCase("rss")) {
		    	result = new RSSExpandedReader().decode(bitmap, hints);
		    }
		    
		    return result.getText();
		}
		catch (Exception e){
			return "null";  //No I18N
		}
	}

}
