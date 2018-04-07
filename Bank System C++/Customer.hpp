/**
 * Customer.hpp
 * Name:
 * Person number:
 *
 * This file contains the definition of the Customer class.
 * Add any fields you wish, but do not change the name of or remove any
 * of the required fields that are provided by default.
 * You may not use any additional headers.
 */

#ifndef A3_CUSTOMER_HPP
#define A3_CUSTOMER_HPP

#include "Transaction.hpp"
#include <algorithm>

class Customer {
public:
    // Used to store the customer ID.
    const size_t _customer_id;

    // Used to store the customer's account balance.
    double _account_balance;

    // List of pending transactions.
    CSE250::dTransactionNode* _pending_txs;

    // Flag to determine if account was overdrawn.
    bool _overdrawn;

    /**
     * Constructor for Customer requires a customer id to be provided.
     * By default, if no starting balance is given, the customer is created with a starting balance of 0.
     * As the member variable _cust_id is const, you must provide this at construction as it cannot be changed later.
     *
     * @param id - the unique customer id number assigned to this customer.
     * @param starting_balance - the dollar amount to start the account at.
     */
    Customer(const size_t& id, const double& starting_balance = 0) : _customer_id(id),
                                                                     _account_balance(starting_balance),
                                                                     _pending_txs(nullptr), _overdrawn(false) { }


    /**
     * Destructor cleans up transaction list, if any remain at the end of execution.
     */
    ~Customer() {
        if (_pending_txs != nullptr) {
            // If transactions still exist at the end of execution, remove them.
            CSE250::dTransactionNode* tempNode = _pending_txs->_next;
            while (_pending_txs != nullptr) {
                delete _pending_txs;
                _pending_txs = tempNode;
                if (_pending_txs != nullptr) {
                    tempNode = _pending_txs->_next;
                }
            }
        }
        _pending_txs = nullptr;
    }

    /**
     * Helper function to add a transaction to a Customer object.
     * Inserts transactions in increasing timestamp ordering.
     * Assumes the transaction timestamp is unique.
     * @param timestamp
     * @param amount
     */
    void add_transaction(const size_t& timestamp, const double& amount) {
        if (_pending_txs == nullptr) {
            // If we currently have no transactions, make the first Transaction node.
            _pending_txs = new CSE250::dTransactionNode(timestamp, amount);
        }
        else {
            // Edge case: check if first node timestamp is larger than the timestamp to insert.
            if (timestamp < _pending_txs->_tx._timestamp) {
                // Set transaction to head of list if timestamp to add is smaller (insert before head).
                _pending_txs->_prev = new CSE250::dTransactionNode(timestamp, amount);
                _pending_txs->_prev->_next = _pending_txs;
                _pending_txs = _pending_txs->_prev;
            }
            else {
                // Otherwise, look through the list for the first spot where the next Transaction has a timestamp
                // that is larger, or we are larger than the end of the list (i.e., next is nullptr).
                CSE250::dTransactionNode* _temp_node = new CSE250::dTransactionNode(timestamp, amount);
                CSE250::dTransactionNode* _current_tx_node = _pending_txs;

                while (_current_tx_node->_next != nullptr && _current_tx_node->_next->_tx._timestamp < timestamp) {
                    _current_tx_node = _current_tx_node->_next;
                }

                // At this point, the timestamp we are trying to add is smaller than the next node,
                // or we have reached the end of the list (_next is a nullptr).
                if (_current_tx_node->_next != nullptr) {
                    // Don't break link going backward.
                    // Establish backward connection to the new node if the next node exists.
                    _current_tx_node->_next->_prev = _temp_node;
                }
                // Link in the new node to the list.
                _temp_node->_next = _current_tx_node->_next;
                _current_tx_node->_next = _temp_node;
                _temp_node->_prev = _current_tx_node;

            }
        }
    }

    /**
     * Helper function to void a transaction in a Customer object.
     * Searches for the transaction to void, if it exists.
     * Assumes the transaction timestamp is unique.
     * @param timestamp - timestamp of transaction requested to void.
     * @return  true - if transaction with given timestamp was found.
     *         false - otherwise.
     */
    bool void_transaction(const size_t& timestamp) {
        if (_pending_txs == nullptr) {
            // If we currently have no transactions, the Transaction to void doesn't exist.
            return false;
        }
        else {
            // Look through the list for the first spot where the current Transaction has a timestamp
            // that is greater than or equal to the one we are seeking, or we are at the end of the list
            // (i.e., current is nullptr).
            CSE250::dTransactionNode* _current_tx_node = _pending_txs;

            while (_current_tx_node != nullptr && _current_tx_node->_tx._timestamp < timestamp) {
                _current_tx_node = _current_tx_node->_next;
            }

            // At this point, the timestamp we are trying to find is greater than or equal to the
            // timestamp of the Transaction in the current node,
            // or we have reached the end of the list (_next is a nullptr).
            if (_current_tx_node == nullptr) {
                // We reached the end of the list.
                return false;
            }
            else {
                // We have a valid node in the list.
                if (_current_tx_node->_tx._timestamp == timestamp) {
                    // We found what we are looking for.
                    // Remove the transaction, relinking the nodes around.
                    if (_current_tx_node->_prev != nullptr) {
                        // If we are not at the head of the list, we need to link a previous node ahead around
                        // the current node.
                        _current_tx_node->_prev->_next = _current_tx_node->_next;
                    }
                    else {
                        // The node we will delete was the head of the list (since _prev is nullptr).
                        // We need to update the head of the list to the next remaining element.
                        // If there is no remaining element (i.e., a list of length 1),
                        // this will correctly set the list to nullptr.
                        _pending_txs = _current_tx_node->_next;
                    }

                    if (_current_tx_node->_next != nullptr) {
                        // If we are not at the end of the list, we need to link a next node back around
                        // the current node.
                        _current_tx_node->_next->_prev = _current_tx_node->_prev;
                    }
                    delete _current_tx_node;
                    return true;
                }
                else {
                    // Transaction we found was greater than the value we were looking for.
                    // Our search has failed.
                    return false;
                }
            }
        }
    }

    /**
     * Helper function to check if a requested Transaction object exists.
     * @param timestamp - timestamp corresponding to the transaction we would like.
     * @return  true - the Transaction at the requested timestamp exists.
     *         false - otherwise.
     */
    bool has_tx_at_time(const size_t& timestamp) const {
        // Look through the list for the first spot where the current Transaction has a timestamp
        // that is greater than or equal to the one we are seeking, or we are at the end of the list
        // (i.e., current is nullptr).
        if (_pending_txs == nullptr) {
            // If we currently have no transactions, the Transaction to void doesn't exist.
            return false;
        }
        else {
            // Look through the list for the first spot where the current Transaction has a timestamp
            // that is greater than or equal to the one we are seeking, or we are at the end of the list
            // (i.e., current is nullptr).
            CSE250::dTransactionNode* _current_tx_node = _pending_txs;

            while (_current_tx_node != nullptr && _current_tx_node->_tx._timestamp < timestamp) {
                _current_tx_node = _current_tx_node->_next;
            }

            // At this point, the timestamp we are trying to find is greater than or equal to the
            // timestamp of the Transaction in the current node,
            // or we have reached the end of the list (_next is a nullptr).
            if (_current_tx_node == nullptr) {
                // We reached the end of the list.
                return false;
            }
            else {
                // We have a valid node in the list.
                if (_current_tx_node->_tx._timestamp == timestamp) {
                    // We found what we are looking for.
                    // Remove the transaction, relinking the nodes around.
                    return true;
                }
                else {
                    // Transaction we found was greater than the value we were looking for.
                    // Our search has failed.
                    return false;
                }
            }
        }
    }

    /**
     * Helper function to obtain a reference to a requested Transaction object.
     * Assumes the transaction timestamp was already inserted.
     * @param timestamp - timestamp corresponding to the transaction we would like.
     * @return const reference to the Transaction object requested.
     */
    const Transaction& get_tx_at_time(const size_t& timestamp) const {
        // Look through the list for the first spot where the current Transaction has a timestamp
        // that is greater than or equal to the one we are seeking, or we are at the end of the list
        // (i.e., current is nullptr).
        CSE250::dTransactionNode* _current_tx_node = _pending_txs;

        while (_current_tx_node->_tx._timestamp != timestamp) {
            _current_tx_node = _current_tx_node->_next;
        }

        // At this point, since we assumed our value was there, we can return the reference.
        return _current_tx_node->_tx;
    }

    bool operator<(const size_t& otherId) const {
        return this->_customer_id < otherId;
    }


private:
    /**
     * Default constructor with no parameters is made private so that no transactions are created without
     * providing a value for the _customer_id.
     */
    Customer();
};


namespace CSE250 {
    class dCustomerIDNode;
}

struct CSE250::dCustomerIDNode {
    // Transaction stored within the node.
    const size_t _customer_id;

    // Pointer to previous node in list.
    dCustomerIDNode* _prev;

    // Pointer to next node in list.
    dCustomerIDNode* _next;

    /**
     * Constructor for a transaction node requires the default information to create a transaction.
     *
     * @param id - the id of a customer of interest.
     */
    dCustomerIDNode(const size_t& id) : _customer_id(id), _prev(nullptr), _next(nullptr) { }

private:
    /**
     * Default constructor with no parameters is made private so that no node is created without
     * providing a value for the _customer_id. This avoids accidentally creating a node without
     * providing a specific id.
     */
    dCustomerIDNode();
};


#endif //A3_CUSTOMER_HPP
