import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

import java.awt.Color;
import java.awt.Point;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;

public class TestCases
{
   public static final double DELTA = 0.00001;

   /* some sample tests but you must write more! see lab write up */
   @Test
   public void testSetCircleColor()
   {
   Circle test_c = new Circle(3.55, new Point(0,0), Color.BLACK);
   assertEquals(3.55, test_c.getRadius(), DELTA);
   }

   @Test
   public void testgetCircleCenter()
   {
   Circle test_c = new Circle(3.55, new Point(0,0), Color.BLACK);
   assertEquals(new Point(0,0), test_c.getCenter());
   }

   @Test
   public void testgetCircleColor()
   {
   Circle test_c = new Circle(3.55, new Point(0,0), Color.BLACK);
   assertEquals(Color.BLACK, test_c.getColor());
   }

   @Test
   public void testCircleGetArea()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(101.2839543, c.getArea(), DELTA);
   }
   
   @Test
   public void testCircleGetPerimeter()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(35.6759261, c.getPerimeter(), DELTA);
   }
   @Test
   public void testCircleTranslate()
   {
   Circle test_c = new Circle(3.55, new Point(1,1), Color.BLACK);
   
   test_c.translate(new Point(3,3));
   assertEquals(new Point(3,3), test_c.getCenter());
   }
   @Test
   public void testRectangleWidth() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      assertEquals(10.0, r.getWidth(), DELTA);
   }

   @Test
   public void testRectangleSetWidth() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      r.setWidth(3.0);
      assertEquals(3.0, r.getWidth(), DELTA);
   }

   @Test
   public void testRectangleHeight() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      assertEquals(5.0, r.getHeight(), DELTA);
   }

   @Test
   public void testRectangleSetHeight() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      r.setHeight(10.0);
      assertEquals(10.0, r.getHeight(), DELTA);
   }

   @Test
   public void testRectangleTopLeft() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      assertEquals(new Point(0, 5), r.getTopLeft());
   }

   @Test
   public void testRectangleColor() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      assertEquals(Color.BLACK, r.getColor());
   }

   @Test
   public void testRectangleSetColor() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      r.setColor(Color.PINK);
      assertEquals(Color.PINK, r.getColor());
   }

   @Test
   public void testRectangleGetArea() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      assertEquals(50.0, r.getArea(), DELTA);
   }

   @Test
   public void testRectangleGetPerimeter() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      assertEquals(30.0, r.getPerimeter(), DELTA);
   }

   @Test
   public void testRectangleTranslate() {
      Rectangle r = new Rectangle(10.0, 5.0, new Point(0, 5), Color.BLACK);
      r.translate(new Point(-1, -5));
      assertEquals(new Point(-1, -5), r.getTopLeft());
   }

   @Test
   public void testTriangleVertexA() {
      Triangle t = new Triangle(new Point(6, 1), new Point(1, 5), new Point(-2, 2), Color.BLACK);
      assertEquals(new Point(6, 1), t.getVertexA());
   }

   @Test
   public void testTriangleVertexB() {
      Triangle t = new Triangle(new Point(6, 1), new Point(1, 5), new Point(-2, 2), Color.BLACK);
      assertEquals(new Point(1, 5), t.getVertexB());
   }

   @Test
   public void testTriangleVertexC() {
      Triangle t = new Triangle(new Point(6, 1), new Point(1, 5), new Point(-2, 2), Color.BLACK);
      assertEquals(new Point(-2, 2), t.getVertexC());
   }

   @Test
   public void testTriangleColor() {
      Triangle t = new Triangle(new Point(6, 1), new Point(1, 5), new Point(-2, 2), Color.BLACK);
      assertEquals(Color.BLACK, t.getColor());
   }

   @Test
   public void testTriangleSetColor() {
      Triangle t = new Triangle(new Point(6, 1), new Point(1, 5), new Point(-2, 2), Color.BLACK);
      t.setColor(Color.PINK);
      assertEquals(Color.PINK, t.getColor());
   }

   @Test
   public void testTriangleArea() {
      Triangle t = new Triangle(new Point(5, 5), new Point(0, 5), new Point(0, 0), Color.BLACK);
      assertEquals(12.5, t.getArea(), DELTA);
   }

   @Test
   public void testTrianglePerimeter() {
      Triangle t = new Triangle(new Point(5, 5), new Point(0, 5), new Point(0, 0), Color.BLACK);
      assertEquals(17.071067811865476, t.getPerimeter(), DELTA);
   }

   @Test
   public void testTriangleTranslate() {
      Triangle t = new Triangle(new Point(6, 1), new Point(1, 5), new Point(-2, 2), Color.BLACK);
      t.translate(new Point(5, 0));
      assertEquals(new Point(11, 1), t.getVertexA());
      assertEquals(new Point(6, 5), t.getVertexB());
      assertEquals(new Point(3, 2), t.getVertexC());
   }

   @Test
   public void testWorkSpaceAreaOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), 
                 Color.BLACK));

      assertEquals(114.2906063, ws.getAreaOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpaceGetCircles()
   {
      WorkSpace ws = new WorkSpace();
      List<Circle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(c1);
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
                 Color.BLACK));
      ws.add(c2);

      expected.add(c1);
      expected.add(c2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getCircles());
   }

   /* HINT - comment out implementation tests for the classes that you have not 
    * yet implemented */
   @Test
   public void testCircleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getRadius", "setRadius", "getCenter", "equals");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, Point.class, boolean.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0], new Class[] {Object.class});

      verifyImplSpecifics(Circle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testRectangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getWidth", "setWidth", "getHeight", "setHeight", "getTopLeft", "equals");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, double.class, void.class, Point.class, boolean.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0], new Class[] {double.class}, 
         new Class[0], new Class[] {Object.class});

      verifyImplSpecifics(Rectangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }
   
   @Test
   public void testTriangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertexA", "getVertexB", "getVertexC", "equals");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class, Point.class, Point.class, boolean.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[0], new Class[0], new Class[] {Object.class});

      verifyImplSpecifics(Triangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   private static void verifyImplSpecifics(
      final Class<?> clazz,
      final List<String> expectedMethodNames,
      final List<Class> expectedMethodReturns,
      final List<Class[]> expectedMethodParameters)
      throws NoSuchMethodException
   {
      assertEquals("Unexpected number of public fields",
         0, clazz.getFields().length);

      final List<Method> publicMethods = Arrays.stream(
         clazz.getDeclaredMethods())
            .filter(m -> Modifier.isPublic(m.getModifiers()))
            .collect(Collectors.toList());

      assertEquals("Unexpected number of public methods",
         expectedMethodNames.size(), publicMethods.size());

      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodReturns.size());
      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodParameters.size());

      for (int i = 0; i < expectedMethodNames.size(); i++)
      {
         Method method = clazz.getDeclaredMethod(expectedMethodNames.get(i),
            expectedMethodParameters.get(i));
         assertEquals(expectedMethodReturns.get(i), method.getReturnType());
      }
   }

}
