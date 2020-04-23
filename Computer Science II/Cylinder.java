package edu.buffalo.cse116;

public class Cylinder extends Circle {

	private double height;
	
	public void setHeight(double h) { height = h; }
	
	public double getHeight() { return height; }
	Cylinder(double rad, double h) {
		setHeight(h);
		setRadius(rad);
	}
	
	public double getVolume() { 
		return (Math.PI * height * (getRadius()*getRadius()));
	}
	
}
