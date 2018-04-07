/**
 * a4.cpp
 * Name: Austin McCarson
 * Person number: 50103630
 *
 * All definitions of functions required for A4 are contained in here.
 * Feel free to add more function definitions to this, but you must
 * include at least the required functions.
 *
 * You may only use the following headers:
 *    <algorithm>, <cstring>, <string>, <vector>, <list>, <stack>,
 *    <queue>, <sstream>, "Tag.hpp"
 */

#include "Tag.hpp"
#include <stack>

std::string erase_whitespace(const std::string& document) {

    std::string newDoc;
    int i = 0;

    while (i < document.size()) {
        if(document[i] == '<') {
            if(document[i+1] != ' ') {
                while (document[i] != '>') {
                    if (document[i] != ' ') {
                        newDoc.push_back(document[i]);
                    }
                    if(document[i] == '/') {
                        while(document[i] != '>') {
                            newDoc.push_back(document[i]);
                            i++;
                        }
                    }
                }
            }
        }
        if (document[i-1] == '>') {
            while (document[i] != '<') {
                if (document[i] != ' ' || document[i] != '\n' || document[i] != '\t') {
                    newDoc.push_back(document[i]);
                }
                i++;
            }
        }
    }
    return newDoc;
}


std::string validTags[16] = {"<html>", "</html>", "<head>", "</head>", "<title>", "</title>", "<body>", "</body>",
                             "<p>", "</p>", "<div>","</div>", "<br>", "<br/>", "<span>", "</span>"};
int validTagsNumber[16] = { 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, 7, 8, -8};


//can use to remove ID for first function and get ID for second function
std::string findID (std::string& tag, std::string id) {

    auto l = static_cast<int>(tag.find('<', 0));

    while (tag[l - 1] != '>') {
        if (tag[l] != tolower(tag[l])) {
            tolower(tag[l]);
            l++;
        }
    }

    auto f = static_cast<int>(tag.find("id", 0));
    int t = 0;

    //check to see if the tag is valid
    while (validTags[t] != tag) {
        if (tag.find("id", 0) != std::string::npos) {

            if (tag.find('"', 0) != std::string::npos) {
                return tag;
            } else {
                //remove the id
                while (tag[f] != '>') {
                    id += tag[f]; /** could i use this in the other functions**/
                    tag[f] = tag[f + 1];
                }
            }
        }

    }
    return tag;
}

/**
 * return true if it is valid code
 * return false if it is invalid code
**/
bool html_is_valid (const std::string& document) {

    std::string erased = erase_whitespace(document);
    int i = 0;
    auto size = static_cast<int>(document.size());
    std::stack<int> stack;


    std::string tag;
    std::string closeTag;// = tag = tag.insert(i, '/')
    auto lastTagPos = document.find("</html>", 0);




    //check to see if the first tag is correct
    auto first = static_cast<int>(erased.find("<!DOCTYPE html>", 0));

    //checks to see if there is anything before the docType tag
    while(erased[i] != first){
        if (erased[i] != ' ' || erased[i] != '\n') {
            return false;
        }
        i++;
    }

    //see if document contains valid html tags
    if(document.find("<head>") == std::string::npos || document.find("</html>") == std::string::npos
       || document.find("<html>") == std::string::npos || document.find("</html>") == std::string::npos
            || document.find("<body>") == std::string::npos || document.find("</body>") == std::string::npos){
        return false;
    }

    auto lastTagEnd = lastTagPos + 7;
    //check to see if there are any chars after the last tag
    while(lastTagEnd != document.size()) {

        if(document[lastTagEnd] != ' ' || document[lastTagEnd] != '\n') {
            return false;
        }
        lastTagEnd++;
    }

    //iterate through document
    int t = 0;
    std::string id;
    int f;
    long l = tag.find('<');
    int tagNum;
    i = 0;
    while(i < size) {
        if(document[i] == '<') {

            //store the tag
            while(document[i-1] != '>') {
                tag += document[i];
                i++;
            }

            while(tag[l-1] != '>') {
                if (tag[l] != tolower(tag[l])) {
                    tolower(tag[l]);
                    l++;
                }
            }

            //run if stack is empty, if tag is the closing tag, pop that open tag from stack
            if(!stack.empty()) {

                if(stack.top() + tagNum == 0) {
                    stack.pop();
                }

            }



            f = static_cast<int>(tag.find("id", 0));

            //check to see if the tag is valid
            while(validTags[t] != tag) {
                if(tag.find("id", 0) != std::string::npos) {

                    if(tag.find("""", 0) != std::string::npos) {
                        return false;
                    }

                    else {
                        //remove the id
                        while(tag[f] != '>') {
                            id += tag[f]; /** could i use this in the other functions**/
                            tag[f] = tag[f+1];
                        }
                    }
                }

                /**can i cast a string to an int or do math with negative numbers stored as strings?**/
                //swap tag with number variable. find number value
                if(validTags[t+1] == tag) {
                    tagNum = validTagsNumber[t+1];

                    //if the tag is not br, then push to stack
                    if(tagNum != validTagsNumber[12]){
                        stack.push(tagNum);
                    }
                }
                if(t == 17) { return false; }
                t++;
            }

        }
        if(stack.empty()) {return true;}

        i++;
    }

    return false;
}

Tag* generate_DOM_tree(const std::string& document) {

    std::string newDoc = erase_whitespace(document);
    int i = 0;
    int n = 0;
    auto size = static_cast<int>(newDoc.size());
    std::string name;
    std::string tag;
    int tagNum; //use to order parent tags, and track stack
    std::string id;
    std::string content;
    std::stack<Tag*> tags;
    //create tags
    Tag* html;
    Tag *head;
    Tag* title;
    Tag* body;
    Tag* p;
    Tag* div;
    Tag* br;
    Tag* span;
    Tag* Content = new Tag("content", "");

    //iterate through document
    while(i > size) {
        //create tag
        if(newDoc[i] == '<') {
            // creates tag
            while (newDoc[i - 1] != '>') {
                tag += newDoc[i];
                i++;
            }
            // starts after end of tag, everything in between > and < is added to content
            content = "";
            while(newDoc[i] != '<') {
                content += newDoc[i];
                i++;
            }
            //create the name
            n = 0;
            if (tag[n] == '<') {
                while (tag[n] != '>' || tag[n,n+1] != 'i','d') {
                    name += tag[n];
                    n++;
                }
            }
             //work on tags
                for (int x = 0; tag != validTags[x]; x++) {
                    if (validTags[x + 1] == tag) {
                        findID(tag, id);
                        tagNum = validTagsNumber[x+1];
                        //html tag stored in html
                        if(tagNum == 1) {
                            html = new Tag(name, id);
                            tags.push(html);
                        }
                        //head tag stored in head, child of html
                        if(tagNum == 2) {
                            head = new Tag(name, id);
                            html->_children[0] = head;
                            tags.push(head);
                        }
                        //title tag stored in title, child of head
                        if(tagNum == 3) {
                            title = new Tag(name, id);
                            if(!content.empty()) {
                                title->_content += content;
                            }
                            head->_children[0] = title;
                            tags.push(title);
                        }
                        //body tag stored in body, child of html
                        if(tagNum == 4) {
                            body = new Tag(name, id);
                            html->_children[1] = body;
                            if(!content.empty()) {
                                body->_content += content;
                            }
                            tags.push(body);
                        }
                        if(tagNum == 5) {
                            p = new Tag(name, id);
                            if(tags.top() == body) {
                                body->_children.push_back(p);
                            }
                            if(tags.top() == div) {
                                div->_children.push_back(p);
                            }
                            if(!content.empty()) {
                                p->_content += content;
                            }
                            tags.push(p);
                        }
                        if(tagNum == 6) {
                            if(tags.top() == body) {
                                div = new Tag(name, id);
                                body->_children.push_back(div);
                            }
                            if(tags.top() == div) {
                                Tag* div1 = tags.top();
                                div = new Tag(name,id);
                                div1->_children.push_back(div);
                            }
                            if(!content.empty()) {
                                div->_content += content;
                            }
                            tags.push(div);
                        }
                        if(tagNum == 7) {
                            br = new Tag(name, id);
                            if(tags.top() == body) {
                                body->_children.push_back(br);
                            }
                            if(tags.top() == p) {
                                p->_children.push_back(br);
                            }
                            if(tags.top() == div) {
                                br->_children.push_back(br);
                            }
                        }
                        if(tagNum == 8) {
                            span = new Tag(name, id);
                            if(tags.top() == body) {
                                body->_children.push_back(span);
                            }
                            if(tags.top() == p) {
                                p->_children.push_back(span);
                            }
                            if(tags.top() == div) {
                                div->_children.push_back(span);
                            }
                            if(!content.empty()) {
                                span->_content += content;
                            }
                            tags.push(span);
                        }
                        if(tagNum == -1) {
                            if(tags.top() == html) {
                                tags.pop();
                            }
                        }
                        if(tagNum == -2) {
                            if(tags.top() == head) {
                                tags.pop();
                            }
                        }
                        if(tagNum == -3) {
                            if(tags.top() == title) {
                                tags.pop();
                            }
                        }
                        if(tagNum == -4) {
                            if(tags.top() == body) {
                                tags.pop();
                            }
                        }
                        if(tagNum == -5) {
                            if(tags.top() == p) {
                                tags.pop();
                            }
                        }
                        if(tagNum == -6) {
                            if(tags.top() == div) {
                                tags.pop();
                            }
                        }
                        if(tagNum == -8) {
                            if(tags.top() == span) {
                                tags.pop();
                            }
                        }
                    }
                }
        }
    }
    return nullptr;
}


void determine_visible_objects(Tag* const root) {

    int i;
    Tag* next;
    Tag* child;
    Tag* nextChild;
    next = root->_children[i];
    child = next->_children[i];
    nextChild = child->_children[i];

    //while(!root->_children.empty()){}

    if(!root->_content.empty()){
        root->_displayed = true;
    }
    if(root->_name != "title" && !root->_content.empty()) {
        root->_displayed = true;
    }
    // TODO: Finish this function.
}

std::string print_visible_elements(Tag* const root) {
    if(root->_displayed) {
        //std::cout << root->_name << std::endl;
        //std::cout << root->_content << std::endl;
    }

    // TODO: Finish this function.
    return "";
}

Tag* getElementByID(Tag* const root, const std::string& id) {
    // TODO: Finish this function.
    return nullptr;
}