---
layout:     post
title:      JSF 登录验证
subtitle:   
date:       2019-02-09 19:25
author:     在到处之间找我
header-img: 
catalog: true
category: JSF
tags:
- JSF
---

- [XHTML 代码](#org1f37b86)
- [backing bean 代码](#org2805e54)
- [注意事项](#orgbcb9870)

本文是一个使用 JSF 组件以及 backing bean 实现判断登录时所输入的用户名以及密码是否存在于数据库中的例子。


<a id="org1f37b86"></a>

# XHTML 代码

XHTML 页面代码如下：

```html
<?xml version='1.0' encoding='UTF-8' ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:h="http://xmlns.jcp.org/jsf/html">
    <h:head>
        <title>Login</title>
    </h:head>
    <h:body>
        <h:form>
            <div>
                <h:outputText value="用户名:"/>
                <h:inputText id="userName"
                             class="form-control"
                             title="请输入你的用户名"
                             value="#{login.userName}"
                             required="true"
                             requiredMessage="用户名必填"
                             maxlength="30"
                             />
                <h:message for="userName" style="color:red"/>
                <br />
            </div>
            <div>
                <h:outputText value="密码:"/>  
                <h:inputSecret id="password"
                               class="form-control"
                               title="请输入你的密码"
                               value="#{login.password}"
                               required="true"
                               requiredMessage="密码必填"
                               validator = "#{login.isLoginSuccess}"
                               maxlength="20"
                               >
                </h:inputSecret>
                <h:message for="password" style="color:red"/>
            </div>

            <div>
                <h:commandButton value="登录" action="#{navBean.home}"></h:commandButton>
            </div>
        </h:form>
    </h:body>
</html>
```


<a id="org2805e54"></a>

# backing bean 代码

对应的 backing bean 代码如下：

```java
import java.util.List;
import javax.faces.application.FacesMessage;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import javax.faces.bean.SessionScoped;
import javax.faces.component.UIComponent;
import javax.faces.component.UIInput;
import javax.faces.component.html.HtmlInputText;
import javax.faces.context.FacesContext;
import javax.faces.validator.ValidatorException;

/**
 *
 * @author ambers
 */
@ManagedBean(name = "login")
@SessionScoped
public class LoginBean {

    private String userName;
    private String password;

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    /**
     * Creates a new instance of LoginBean
     */
    public LoginBean() {
    }

    public void isLoginSuccess(FacesContext context, UIComponent component, Object value) throws ValidatorException {
        UIComponent c = null;

        for (UIComponent ui : component.getParent().getChildren()) {
            if ("userName".equals(ui.getId())) {    //这里的"userName"是输入用户名控件的id
                c = ui;
                break;
            }
        }

        HtmlInputText htmlInputText = (HtmlInputText) c;

        String name = htmlInputText.getValue().toString().trim();
        String pass = value.toString().trim();

        System.out.println("获取到的userName的值为：" + name);
        User user = ufl.find(name);   //这句的意思是在数据库里查找输入的用户名，并返回一个实体类。这只是我的方法，每个人的可能略有差别。

        if (user == null) {   //不存在该用户名
            FacesMessage msg = new FacesMessage("不存在该用户名！");
            throw new ValidatorException(msg);
        } else if (!user.getPassword().equals(pass)) {  //密码错误
            FacesMessage msg = new FacesMessage("密码错误！");
            throw new ValidatorException(msg);
        }
    }
}
```


<a id="orgbcb9870"></a>

# 注意事项

这里的难点是如何在密码输入框的 validator 中获取到用户名输入框的内容，本例采取的方法是通过组件树搜索的方法得到的。

还有一点要注意的是 validator 中的函数是不带括号的：

```java
validator = "#{login.isLoginSuccess}"
```

也就是说，写成下面是错误的（不管怎么样，我试的是不行的）

```java
validator = "#{login.isLoginSuccess()}"
```

在我的下篇博文中将为大家讲解如何在注册的时候实现二次密码判断。