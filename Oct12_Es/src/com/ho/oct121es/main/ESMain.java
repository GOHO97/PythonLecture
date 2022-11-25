package com.ho.oct121es.main;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ESMain {
	public static void main(String[] args) {
		HttpURLConnection huc = null;
		try {
			
			URL u = new URL("http://192.168.0.125:9200/oct12_hangul_kwon/_search");
			huc = (HttpURLConnection) u.openConnection();
			huc.setRequestMethod("POST");
			huc.setRequestProperty("Content-Type", "application/json;charset=utf-8");
			// 우리 요청 내용이 JSON이다라는 것.
			huc.setDoOutput(true);
			String reqBody = "{\"query\":{\"match\": {\"chat\": \"귀요미\"}}}";
			
			OutputStream os = huc.getOutputStream();
			byte[] reqBody2 = reqBody.getBytes("utf-8");
			os.write(reqBody2, 0, reqBody2.length);
			
			InputStream is = huc.getInputStream();
			InputStreamReader isr = new InputStreamReader(is, "utf-8");
			BufferedReader br = new BufferedReader(isr);
			String line = null;
			
			while((line = br.readLine()) != null) {
				System.out.println(line);
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		huc.disconnect();
	}
}
