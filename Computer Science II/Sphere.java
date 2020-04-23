package edu.buffalo.cse116;

public class Sphere extends Circle {

	Sphere(double rad) {
		setRadius(rad);
	}
	
	public double getArea() {
		return Double.NaN;
	}
	
	public double getVolume() {
		return ((4.00/3.00)*Math.PI*getRadius()*getRadius()*getRadius());
	}
	
}
