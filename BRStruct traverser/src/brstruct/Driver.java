package brstruct;

public class Driver {
	public static void main(String[] args) {
		BRStruct<String> tree = new BRStruct<String>(); tree.insertRoot("Mammal");
		BRStruct<String> tL = new BRStruct<String>(); tL.insertRoot("Cat");
		BRStruct<String> tR = new BRStruct<String>(); tR.insertRoot("Dog");
		tree.setLeft(tL); tree.setRight(tR);
		BRStruct<String> t1 = new BRStruct<String>(); t1.insertRoot("A");
		BRStruct<String> t2 = new BRStruct<String>(); t2.insertRoot("B");
		BRStruct<String> t3 = new BRStruct<String>(); t3.insertRoot("C");
		tL.setLeft(t1);
		t1.setLeft(t2);
		t2.setLeft(t3);
		System.out.println(tree);
	}
}
