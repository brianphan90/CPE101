import java.awt.*;

public class Triangle implements Shape{
    private Point vertexA;
    private Point vertexB;
    private Point vertexC;
    private Color color;

    public Triangle(Point vertexA, Point vertexB, Point vertexC, Color color) {
        this.vertexA = vertexA;
        this.vertexB = vertexB;
        this.vertexC = vertexC;
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
        double first_l = Math.sqrt(Math.pow((this.vertexB.getX() - this.vertexA.getX()), 2) + Math.pow((this.vertexB.getY() - this.vertexA.getY()), 2));
        double second_l = Math.sqrt(Math.pow((this.vertexC.getX() - this.vertexB.getX()), 2) + Math.pow((this.vertexC.getY() - this.vertexB.getY()), 2));
        double third_l = Math.sqrt(Math.pow((this.vertexC.getX() - this.vertexA.getX()), 2) + Math.pow((this.vertexC.getY() - this.vertexA.getY()), 2));

        double perim = first_l + second_l + third_l;
        return perim;
    }

    @Override
    public void translate(Point p) {
    vertexA.x += p.x;
    vertexA.y += p.y;
    vertexB.x += p.x;
    vertexB.y += p.y;
    vertexC.x += p.x;
    vertexC.y += p.y;
    }
    public boolean equals(Object other){
        if(other == null){
            return false;
        }
        if(this.getClass() != other.getClass()){
            return false;
        }
        if(this.vertexA != ((Triangle)other).vertexA){
            return false;
        }
        if (this.vertexB != ((Triangle)other).vertexB){
            return false;
        }
        if (this.vertexC != ((Triangle)other).vertexC){
            return false;
        }
        if (this.color != ((Triangle)other).color){
        }
    return true;
    }
}
