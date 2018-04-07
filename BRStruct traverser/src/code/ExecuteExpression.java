package code;

import java.beans.Expression;

import brstruct.BRStruct;
import brstruct.BRStruct.IAlgo;

//Austin McCarson, Fall 2014

//Execute expressions at each node
public class ExecuteExpression implements IAlgo<Integer, Expression, Object> {

	@Override
	public Integer emptyCase(BRStruct<Expression> host, Object arg) {
		return 0;
	}

	@Override
	public Integer nonEmptyCase(BRStruct<Expression> host, Object arg) {
		return host.getLeft().execute(this, arg) + host.getRight().execute(this, arg);
	}
	
	
	
}
