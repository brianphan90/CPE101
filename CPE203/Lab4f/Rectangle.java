import java.awt.*;

public class Rectangle implements Shape {
    private double width;
    private double height;
    private Point topLeft;
    private Color color;
    public Rectangle(double width, double height, Point topLeft, Color color){
        this.width = width;
        this.height = height;
        this.topLeft = topLeft;
        this.color = color;
    }
    public double getWidth(){
        return width;
    }
    public void setWidth(double new_width){
        width = new_width;
    }
    public double getHeight(){
        return height;
    }
    public void setHeight(double new_height){
        height = new_height;
    }
    public Point getTopLeft(){
        return topLeft;
    }

    @Override
    public Color getColor() {
        return color;
    }

    @Override
    public void setColor(Color c) {
        color = c;
    }

    @Override
    public double getArea() {
        return width * height;
    }

    @Override
    public double getPerimeter() {
        return (2 * width + 2 * height);
    }

    @Override
    public void translate(Point p) {
        topLeft = p;
    }
    public boolean equals(Object other){
        if(other == null){
            return false;
        }
        if(this.getClass() != other.getClass()){
            return false;
        }
        if(this.width != ((Rectangle)other).width){
            return false;
        }
        if (this.height != ((Rectangle)other).height){
            return false;
        }
        if (this.topLeft != ((Rectangle)other).topLeft){
            return false;
        }
        if (this.color != ((Rectangle)other).color){
            return false;
        }
    return true;
    }
}
