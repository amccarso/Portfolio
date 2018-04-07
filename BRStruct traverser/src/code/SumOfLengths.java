package code;

import brstruct.BRStruct;
import brstruct.BRStruct.IAlgo;

//Austin McCarson, Fall 2014

//Returns some of all strings in node
public class SumOfLengths implements IAlgo<Integer, String, Object> {

	@Override
	public Integer emptyCase(BRStruct<String> host, Object arg) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public Integer nonEmptyCase(BRStruct<String> host, Object arg) {
		return 1 + host.getLeft().getDatum().length() + host.getRight().getDatum().length();
	}

}
