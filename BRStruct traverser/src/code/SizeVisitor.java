package code;

import brstruct.BRStruct;
import brstruct.BRStruct.IAlgo;

//Austin McCarson, Fall 2014

//Get size of struct
public class SizeVisitor implements IAlgo<Integer, Integer, Object> {

	@Override
	public Integer emptyCase(BRStruct<Integer> host, Object arg) {
		return 0;
	}

	@Override
	public Integer nonEmptyCase(BRStruct<Integer> host, Object arg) {
		return 1 + host.getLeft().execute(this, arg) + host.getRight().execute(this, arg);
	}
	

}
