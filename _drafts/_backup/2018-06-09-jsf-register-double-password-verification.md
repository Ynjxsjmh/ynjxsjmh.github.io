---
layout:     post
title:      JSF 实现注册时的二次密码验证 
subtitle:   
date:       2019-02-09 19:52
author:     在到处之间找我
header-img: 
catalog: true
tags:
- jsf
---

- [HTML 代码](#orgb534635)
- [backing bean 代码](#org27d409c)

在我的上篇博文中已经为大家讲解了如何使用 JSF 实现登录时验证用户名和密码是否匹配的问题

在这篇博文中，我将使用类似的方法为大家实现注册时二次验证密码的功能。


<a id="orgb534635"></a>

# HTML 代码

注册页面

```html
<?xml version='1.0' encoding='UTF-8' ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:h="http://xmlns.jcp.org/jsf/html"
      xmlns:f="http://xmlns.jcp.org/jsf/core">
    <h:head>
        <title>Register</title>
    </h:head>
    <h:body>
        <h:form>
            <div>
                <h:outputText value="密码:"/>  
                <h:inputSecret id="password"
                               title="请输入你的密码"
                               value="${register.password}"
                               required="true"
                               requiredMessage="密码必填"
                               maxlength="20"
                               />
                <h:message for="password" style="color:red"/>
                <br/>
            </div>
            <div class="form-group">
                <h:outputText value="确认密码:" />
                <h:inputSecret id="confirmPassword"
                               value="#{register.passwordConfirm}"
                               title="请再次输入你的密码" 
                               required="true"  
                               requiredMessage="请确认密码"
                               validator = "#{register.isPasswordRight}"
                               />
                <h:message for="confirmPassword" style="color:red"/>
                <br/>
            </div>
            <div>
                <h:commandButton  id="register" value="注册"></h:commandButton>                        
            </div>
        </h:form>        
    </h:body>
</html>
```


<a id="org27d409c"></a>

# backing bean 代码

对应的 backing bean

```java
import javax.faces.application.FacesMessage;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import javax.faces.component.UIComponent;
import javax.faces.component.html.HtmlInputSecret;
import javax.faces.component.html.HtmlInputText;
import javax.faces.context.FacesContext;
import javax.faces.validator.ValidatorException;

/**
 *
 * @author ambers
 */
@ManagedBean(name = "register")
@RequestScoped
public class RegisterBean {

    private String password;
    private String passwordConfirm;

    /**
     * Creates a new instance of RegisterBean
     */
    public RegisterBean() {
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getPasswordConfirm() {
        return passwordConfirm;
    }

    public void setPasswordConfirm(String passwordConfirm) {
        this.passwordConfirm = passwordConfirm;
    }

     public void isPasswordRight(FacesContext context, UIComponent component, Object value) throws ValidatorException {
        UIComponent c = null;

        for (UIComponent ui : component.getParent().getChildren()) {
            if ("password".equals(ui.getId())) {
                c = ui;
                break;
            }
        }

        HtmlInputSecret htmlInputSecret = (HtmlInputSecret) c;
        if (!value.toString().trim().equals(htmlInputSecret.getValue().toString().trim())) {
            FacesMessage msg = new FacesMessage("两次输入密码不一致！");
            throw new ValidatorException(msg);
        }
    }   
}
```

按我的上篇博文中所讲的方法大家可以不难写出上述的代码。