package coursework1;

// Question A
public class ConvexHull {
	
	public static Coordinate[] createPoints(int numberOfPoints) {
		Coordinate point[] = new Coordinate[numberOfPoints];
		int min = 1;
		int max = 100;
		for(int i=0;i<point.length; i++) {
			int x = (int) (Math.random() * (max - min + 1) + min);
			int y = (int) (Math.random() * (max - min + 1) + min);
			point[i] = new Coordinate(x,y);
		}
		return point;
	}
	
	public static void main(String[] args) {
			
		// creating random points 
		Coordinate[] points = createPoints(30);
		GiftWrapping gfa = new GiftWrapping();
		
		gfa.convexHull(points);
	}

}

