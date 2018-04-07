package code;

import brstruct.BRStruct;
import brstruct.BRStruct.IAlgo;

//Austin McCarson, Fall 2014

//Gets height of struct
public class HeightVisitor implements IAlgo<Integer, Integer, Object> {

	@Override
	public Integer emptyCase(BRStruct<Integer> host, Object arg) {
		return -1;
	}

	@Override
	public Integer nonEmptyCase(BRStruct<Integer> host, Object arg) {
		return 1 + Math.max(host.getLeft().execute(this, arg), host.getRight().execute(this, arg));
	}

}
