package com.ho.oct121es.main;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;

import co.elastic.clients.elasticsearch.ElasticsearchClient;
import co.elastic.clients.elasticsearch.core.IndexRequest;
import co.elastic.clients.elasticsearch.core.IndexResponse;
import co.elastic.clients.json.jackson.JacksonJsonpMapper;
import co.elastic.clients.transport.rest_client.RestClientTransport;

public class ESMain2 {
	public static void main(String[] args) {
		try {
			HttpHost hh = new HttpHost("192.168.0.125", 9200);
			RestClientBuilder rcb = RestClient.builder(hh);
			RestClient rc = rcb.build();
			JacksonJsonpMapper jjm = new JacksonJsonpMapper();
			RestClientTransport rct = new RestClientTransport(rc, jjm);
			ElasticsearchClient ec = new ElasticsearchClient(rct);
			// 주소 연결하고 
			
			System.out.println("ok");
			
			Menu m = new Menu("야채김밥", 4000);
			
			IndexRequest.Builder<Menu> irb = new IndexRequest.Builder<>();
			irb.index("oct12_menu").document(m);
			
			IndexResponse ir = ec.index(irb.build());
			System.out.println(ir.toString());
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
