package com.ho.oct121es.main;

import java.util.List;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;

import co.elastic.clients.elasticsearch.ElasticsearchClient;
import co.elastic.clients.elasticsearch.core.SearchRequest;
import co.elastic.clients.elasticsearch.core.SearchResponse;
import co.elastic.clients.elasticsearch.core.search.Hit;
import co.elastic.clients.json.jackson.JacksonJsonpMapper;
import co.elastic.clients.transport.rest_client.RestClientTransport;

public class ESMain3 {
	public static void main(String[] args) {
		try {
			HttpHost hh = new HttpHost("192.168.0.125", 9200);
			RestClientBuilder rcb = RestClient.builder(hh);
			RestClient rc = rcb.build();
			JacksonJsonpMapper jjm = new JacksonJsonpMapper();
			RestClientTransport rct = new RestClientTransport(rc, jjm);
			ElasticsearchClient ec = new ElasticsearchClient(rct);
			
			SearchRequest.Builder srb = new SearchRequest.Builder();
			// 값 가져오기는 SearchRequest로
			srb.index("oct12_menu");
			// index 셋팅
			
			SearchResponse<Menu> sr = ec.search(srb.build(), Menu.class);
			// srb를 build로 만들고 Menu라는 클래스 형태로 받아올 것이라는 것을 알려줌.
			
			List<Hit<Menu>> menus = sr.hits().hits();
			// 엘라스틱서치에서 찾아온 데이터를 Hit라는 리스트로 반환하기 때문에 위 처럼 받아준다.
			
			for (Hit<Menu> m : menus) {
				System.out.println(m.toString());
			}
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
