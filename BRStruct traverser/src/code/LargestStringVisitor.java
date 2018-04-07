package code;

import brstruct.BRStruct;
import brstruct.BRStruct.IAlgo;

//Austin McCarson, Fall 2014

//Find largest string in struct
public class LargestStringVisitor implements IAlgo<String, String, Object> {

	@Override
	public String emptyCase(BRStruct<String> host, Object arg) {
		return "";
	}

	@Override
	public String nonEmptyCase(BRStruct<String> host, Object arg) {
		Integer _right = host.getRight().getDatum().length();
		Integer _left = host.getLeft().getDatum().length();
		Integer _datum = host.getDatum().length();
		
		if(_right > _left){
			return host.getRight().toString();
		}
		
		if(_right > _datum){
			return host.getRight().toString();
		}
		
		return null;
	}

}
