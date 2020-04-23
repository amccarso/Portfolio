package edu.buffalo.cse116;

public class Circle {

	private double radius;
	
	Circle(){}
	Circle(double rad) {
		radius = rad;
	}
	
	public double getRadius() {
		return radius;
	}
	
	public void setRadius(double rad) {
		radius = rad;
	}
	
	public double getArea() {
		return Math.PI*(radius*radius);
	}
	
}
