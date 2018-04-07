/**
 * BankData.cpp
 * Name:
 * Person number:
 *
 * All definitions of functions for the class BankData and the description of all methods are contained in here.
 * Feel free to add more function definitions to this, but you must include at least the required methods.
 * You may not use any additional headers.
 */


#include "BankData.hpp"

bool compCustomerPointers(const Customer* const &  lhs, const size_t & rhs) {
    return lhs->_customer_id < rhs;
}

/**
 * Add a customer to the stored customers if no customer with the same id is present.
 *
 * @param customer_id - id to assign the new customer.
 * @param balance - starting balance for the customer.
 * @return  true - if customer was successfully added.
 *         false - if the customer was previously added.
 */
bool BankData::add_customer(const size_t& customer_id, const double& balance) {
    // Returns an iterator pointing to the first element in the range [begin,end)
    // which does not compare less than customer_id.
    // Returns end if every value is smaller or no elements are in range.
    auto insert_point = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);

    // Edge case: iterator returned is the end of the list.
    if (insert_point == _customers.end()) {
        // Every customer had an ID that was smaller, or no customers were inserted yet.
        // Insert the customer.
        _customers.insert(insert_point, new Customer(customer_id, balance));
        // Return true.
        return true;
    }
    else {
        // Otherwise, check if the value found was equal or larger than customer_id.
        if ((*insert_point)->_customer_id == customer_id) {
            // We already have a customer with the ID requested to be inserted.
            // Return false.
            return false;
        }
        else {
            // The Customer we found has an ID larger than the customer_id
            // we want to create, so we want to insert before it.
            // This will maintain a sorted order from smallest to largest customer ID.
            _customers.insert(insert_point, new Customer(customer_id, balance));
            return true;
        }
    }
}

/**
 * Add a list of customers to the stored customers with the ids within this list.
 * You should initialize the customers with an account balance of 0.
 * All values in the list should be processed, even if a customer already exists.
 *
 * @param customer_list - list of customer ids to add.
 * @return  true - if all customers were successfully added.
 *         false - if some customer was previously added (including if there are duplicates in the list itself).
 */
bool BankData::add_customer(const CSE250::dCustomerIDNode* customer_list) {
    bool returnValue = true;
    while (customer_list != nullptr) {
        // Take the result of adding AND'ed with the current return value.
        // If returnValue ever becomes false, the false value will persist from that point on.
        // We need to put " && returnValue" after the call to add_customer,
        // since the remaining values should be added.
        // Putting "returnValue && " would short circuit the statement and the function call would be skipped.
        returnValue = add_customer(customer_list->_customer_id) && returnValue;
        customer_list = customer_list->_next;
    }
    return returnValue;
}

/**
 * Remove a customer from the stored customers.
 *
 * @param customer_id - id of customer to remove.
 * @return  true - if customer was successfully removed.
 *         false - if the customer was not present.
 */
bool BankData::remove_customer(const size_t& customer_id) {
    // Returns an iterator pointing to the first element in the range [begin,end)
    // which does not compare less than customer_id.
    // Returns end if every value is smaller or no elements are in range.
    auto remove_point = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);

    // Edge case: iterator returned is the end of the list.
    if (remove_point == _customers.end()) {
        // Every customer had an ID that was smaller, or no customers were inserted yet.
        // Removal failed since the customer was not found.
        // Return false.
        return false;
    }
    else {
        // Otherwise, check if the value found was equal or larger than customer_id.
        if ((*remove_point)->_customer_id == customer_id) {
            // We have a customer with the ID requested to be removed.
            // Remove the customer.
            delete *remove_point;
            _customers.erase(remove_point);

            // Return true since removal was successful.
            return true;
        }
        else {
            // The Customer we found has an ID larger than the customer_id
            // we want to remove, so we do not have a customer with the appropriate ID.
            // Return false since removal failed.
            return false;
        }
    }
}

/**
 * Remove a list of customer to the stored customers with an account balance of 0.
 * All values in the list should be processed, even if an ID is for a customer that
 * was already removed or doesn't exist.
 *
 * @param customer_list - list of customer ids to remove.
 * @return  true - if all customers were successfully removed.
 *         false - if some customer was not removed (including if there are duplicates in the list itself).
 */
bool BankData::remove_customer(const CSE250::dCustomerIDNode* customer_list) {
    bool returnValue = true;
    while (customer_list != nullptr) {
        // Take the result of removing AND'ed with the current return value.
        // If returnValue ever becomes false, the false value will persist from that point on.
        // We need to put " && returnValue" after the call to remove_customer,
        // since the remaining values should be removed.
        // Putting "returnValue && " would short circuit the statement and the function call would be skipped.
        returnValue = remove_customer(customer_list->_customer_id) && returnValue;
        customer_list = customer_list->_next;
    }
    return returnValue;
}

/**
 * Add a transaction for to the transaction list for the specified customer.
 *
 * You may assume that each timestamp will be unique between each call to process transactions.
 *
 * @param customer_id - id of the customer to add the transaction under.
 * @param timestamp - timestamp the transaction should be created with.
 * @param amount - amount the transaction will change their account balance
 * @return  true - if the transaction was successfully added to the customer's account.
 *         false - if the customer didn't exist.
 */
bool BankData::add_transaction(const size_t& customer_id, const size_t& timestamp, const double& amount) {
    // Returns an iterator pointing to the first element in the range [begin,end)
    // which does not compare less than customer_id.
    auto add_point = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);

    if (add_point == _customers.end()) {
        // Every customer had an ID that was smaller, or no customers were inserted yet.
        // Return false.
        return false;
    }
    else {
        if ((*add_point)->_customer_id == customer_id) {
            // If the value found was the customer_id,
            // then we need to add the Transaction to the customer's list.
            (*add_point)->add_transaction(timestamp, amount);
            return true;
        }
        else {
            // Otherwise, the value found was larger than customer_id so the customer doesn't exist.
            return false;
        }
    }
}

/**
 * Void the transaction with the specified customer id and timestamp
 * (i.e., remove it from the customer's transaction list).
 *
 * @param customer_id - id of the customer the transaction is under.
 * @param timestamp - timestamp the transaction was created with.
 * @return  true - if the transaction was successfully added to the customer's account.
 *         false - if the customer didn't exist or there is no transaction with the given timestamp
 *                 for that customer.
 */
bool BankData::void_transaction(const size_t& customer_id, const size_t& timestamp) {
    // Returns an iterator pointing to the first element in the range [begin,end)
    // which does not compare less than customer_id.
    auto void_point = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);
    if (void_point == _customers.end()) {
        // Every customer had an ID that was smaller, or no customers were inserted yet.
        // Return false.
        return false;
    }
    else {
        if ((*void_point)->_customer_id == customer_id) {
            // If the value found was the customer_id,
            // then we need to void the Transaction in the customer's list.
            return (*void_point)->void_transaction(timestamp);
        }
        else {
            // Otherwise, the value found was larger than customer_id so the customer doesn't exist.
            return false;
        }
    }
}

/**
 * Process each transaction for each customer.
 * At the end, all transaction lists should be empty and account balances should reflect all changes
 * dictated by the respective lists of transactions.
 * Create a list of all customers that had overdrawn their account.
 * @return double linked list of all customer IDs that overdrew their account.
 */
CSE250::dCustomerIDNode* BankData::process_transactions() {
    CSE250::dCustomerIDNode* custList = nullptr;
    CSE250::dCustomerIDNode* currentNode = nullptr;
    bool addToList = false;
    for(Customer* const customer : _customers) {
        addToList = false;
        while(customer->_pending_txs != nullptr) {
            customer->_account_balance += customer->_pending_txs->_tx._tx_amt;
            if(customer->_account_balance < 0) {
                customer->_overdrawn = true;
                addToList = true;
            }
            auto temp = customer->_pending_txs->_next;
            delete customer->_pending_txs;
            customer->_pending_txs = temp;
        }

        if(addToList) {
            if(custList == nullptr) {
                custList = new CSE250::dCustomerIDNode(customer->_customer_id);
                currentNode = custList;
            }
            else {
                currentNode->_next = new CSE250::dCustomerIDNode(customer->_customer_id);
                currentNode->_next->_prev = currentNode;
                currentNode = currentNode->_next;
            }
        }
    }
    return custList;
}


/**
 * Process each transaction for a single customer.
 * While processing the transactions, if the customer's balance becomes negative,
 * then the _overdrawn flag should be set to true.
 *
 * @param customer - customer object for which to process transactions.
 */
void BankData::process_transactions(Customer& customer) {
    while(customer._pending_txs != nullptr) {
        customer._account_balance += customer._pending_txs->_tx._tx_amt;
        if(customer._account_balance < 0) {
            customer._overdrawn = true;
        }
        auto temp = customer._pending_txs->_next;
        delete customer._pending_txs;
        customer._pending_txs = temp;
    }
}

/**
 * Tell whether or not a customer with the specified ID exists in the stored customer data.
 *
 * @param customer_id -  id of the customer requested.
 * @return  true - if the customer requested has a stored record.
 *         false - otherwise.
 */
bool BankData::customer_exists(const size_t& customer_id) {
    // Returns an iterator pointing to the first element in the range [begin,end)
    // which does not compare less than customer_id.
    // Returns end if every value is smaller or no elements are in range.
    auto find_point = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);

    // Edge case: iterator returned is the end of the list.
    if (find_point == _customers.end()) {
        // Every customer had an ID that was smaller, or no customers were inserted yet.
        // Return false.
        return false;
    }
    else {
        // Otherwise, check if the value found was equal or larger than customer_id.
        if ((*find_point)->_customer_id == customer_id) {
            // We found the customer with the ID requested.
            // Return true.
            return true;
        }
        else {
            // The Customer we found has an ID larger than the customer_id we seek.
            // Therefore, the customer was not found.
            // Return false.
            return false;
        }
    }
}

/**
 * Tell whether or not the ID belongs to a valid customer and
 * the timestamp belongs to a valid Transaction under that customer.
 *
 * @param customer_id -  id of the customer requested.
 * @param timestamp - timestamp the transaction was created with.
 * @return  true - if the customer requested has a stored record.
 *         false - otherwise.
 */
bool BankData::transaction_exists(const size_t& customer_id, const size_t& timestamp) {
    if (customer_exists(customer_id)) {
        // If the customer exists, we can request a reference to the Customer.
        const Customer& customer = this->get_customer_data(customer_id);
        // Pass call on to the function within the customer to check if the Transaction exists.
        return customer.has_tx_at_time(timestamp);
    }
    else {
        // If the customer for the given ID doesn't exist, return false.
        return false;
    }
}

/***********************************************************************************************/
/* The following definitions cannot be completed until you decide how you will store your data.*/
/***********************************************************************************************/

/**
 * Get access to the customer data associated with the requested ID.
 * You should assume that the ID belongs to a valid customer.
 * @param customer_id - id of the customer requested.
 * @return constant reference to the Customer object associated with the id.
 */
const Customer& BankData::get_customer_data(const size_t& customer_id) {
    auto result = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);
    return *(*result);
}

/**
 * Get access to the transaction data associated with the requested ID and timestamp.
 * You should assume that the ID belongs to a valid customer and the timestamp belongs to a valid Transaction.
 * @param customer_id - id of the customer requested.
 * @param timestamp - timestamp the transaction was created with.
 * @return constant reference to the Transaction object associated with the id and timestamp.
 */
const Transaction& BankData::get_customer_transaction(const size_t& customer_id, const size_t& timestamp) {
    auto result = std::lower_bound(_customers.begin(), _customers.end(), customer_id, compCustomerPointers);
    return (*result)->get_tx_at_time(timestamp);
}
