package code;

import code.LRStruct.IAlgo;

public class LRConcat implements IAlgo<String, String, Object> {

	@Override
	public String emptyCase(LRStruct<String> host, Object arg) {
		// TODO Auto-generated method stub
		return "";
	}

    //Concatenate all strings in struct
	@Override
	public String nonEmptyCase(LRStruct<String> host, Object arg) {
		// TODO Auto-generated method stub
		return host.getDatum().concat(host.getRest().toString());
	} 

}
