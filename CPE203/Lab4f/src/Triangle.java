import java.awt.*;

public class Triangle implements Shape{
    private Point vertexA;
    private Point vertexB;
    private Point vertexC;
    private Color color;

    public Triangle(Point vertexA, Point vertexB, Point VertexC, Color color) {
        this.vertexA = vertexA;
        this.vertexB = vertexB;
        this.vertexC = VertexC;
        this.color = color;
    }
    public Point getVertexA(){
        return vertexA;
    }
    public Point getVertexB(){
        return vertexB;
    }
    public Point getVertexC(){
        return vertexC;
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
        return 0.5*(vertexC.x * ( vertexA.y - vertexB.y)+ vertexB.x*(vertexC.y - vertexA.y ) + vertexA.x*(vertexB.y-vertexC.y));
    }

    @Override
    public double getPerimeter() {
        return 0;
    }

    @Override
    public void translate(Point p) {
    vertexA.x += p.x;
    vertexA.y += p.y;
    vertexB.x += p.x;
    vertexB.y += p.y;
    vertexC.y += p.x;
    vertexC.y += p.y;
    }
}
