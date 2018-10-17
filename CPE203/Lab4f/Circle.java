import java.awt.*;

public class Circle implements Shape {
    private double radius;
    private Point center;
    private Color color;

    public Circle(double radius, Point center, Color color) {
        this.radius = radius;
        this.center = center;
        this.color = color;
    }
    public double getRadius(){
        return radius;
    }
    public void setRadius(double new_radius){
        radius = new_radius;
    }
    public Point getCenter(){
        return center;
    }

    @Override
    public Color getColor() {
        return color;
    }

    @Override
    public void setColor(Color new_color) {
        color = new_color;
    }

    @Override
    public double getArea() {
        return Math.PI * Math.pow(radius, 2.0);
    }

    @Override
    public double getPerimeter() {
        return Math.PI * 2 * radius;
    }

    @Override
    public void translate(Point p) {
        center = p;
    }
    public boolean equals(Object other){
        if(other == null){
            return false;
        }
        if(this.getClass() != other.getClass()){
            return false;
        }
        if(this.radius != ((Circle)other).radius){
            return false;
        }
        if (this.center != ((Circle)other).center){
            return false;
        }
        if (this.color != ((Circle)other).color){
            return false;
        }
       
    return true;
    }
}
