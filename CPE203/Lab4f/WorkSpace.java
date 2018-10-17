import java.awt.Color;
import java.util.*;
public class WorkSpace {
    private ArrayList<Shape> objects;
    public WorkSpace(){
        this.objects = new ArrayList<Shape>();
    }
    public void add(Shape shape){
        objects.add(shape);
    }
    public Shape get(int index){
        return objects.get(index);
    }
    public int size(){
        return objects.size();
    }
    public List<Circle> getCircles(){
        ArrayList<Circle> c = new ArrayList<Circle>();
        for(Shape object: objects){
            if(object instanceof Circle){
                c.add((Circle) object); //type cast to circle from shape class
            }
        }
        return c;
    }
    public List<Rectangle> getRectangles(){
        ArrayList<Rectangle> r = new ArrayList<Rectangle>();
        for(Shape object : objects){
            if(object instanceof Rectangle){
                r.add((Rectangle)object);   //type cast to rectangle
            }
        }
        return r;
    }

    public List<Triangle> getTriangles(){
        ArrayList<Triangle> t = new ArrayList<Triangle>();
        for(Shape object : objects){
            if(object instanceof Triangle){
                t.add((Triangle)object);   //type cast to rectangle
            }
        }
        return t;
    }
    public List<Shape> getShapesByColor(Color color){
        ArrayList<Shape> color_l = new ArrayList<Shape>();
        for(Shape object : objects){
            if(object.getColor() == color)
                color_l.add(object);
        }
        return color_l;
    }
    public double getAreaOfAllShapes(){
        double tot_area = 0;
        for(Shape object:objects){
            tot_area += object.getArea();
        }
        return tot_area;
    }
    public double getPerimeterofAllShapes(){
        double tot_perimeter = 0;
        for(Shape object:objects){
            tot_perimeter += object.getPerimeter();
        }
        return tot_perimeter;
    }
}
