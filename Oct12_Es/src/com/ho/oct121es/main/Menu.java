package com.ho.oct121es.main;

// mybatis 느낌으로 저걸 표현할 수 있게끔 자바빈을 만들어주는 것이다.
public class Menu {
	private String name;
	private int price;
	
	
	public Menu() {
		// TODO Auto-generated constructor stub
	}

	public Menu(String name, int price) {
		super();
		this.name = name;
		this.price = price;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}
	
}
