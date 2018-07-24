/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.patch.annotaion.Add
 *  com.meituan.sample.SecondActivity
 *  com.meituan.sample.robusttest.o
 */
package com.meituan.sample.robusttest;

import com.meituan.robust.patch.SecondActivityInLinePatch;
import com.meituan.robust.patch.annotaion.Add;
import com.meituan.sample.SecondActivity;
import com.meituan.sample.robusttest.o;

@Add
public class InnerTest {
    public String field = "Innertest";

    public String getTextI1(String string) {
        string = new SecondActivityInLinePatch((Object)new SecondActivity()).getTextI2("asdasd");
        return "asdasd";
    }
}

