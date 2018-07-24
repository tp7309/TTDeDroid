/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.patch.annotaion.Add
 */
package com.meituan.sample.robusttest;

import com.meituan.robust.patch.ImageQualityUtilInLinePatch;
import com.meituan.robust.patch.annotaion.Add;

@Add
public class NewAddCLass {
    public static String get() {
        new ImageQualityUtilInLinePatch(null);
        return ImageQualityUtilInLinePatch.getLargeUrl("asdasd");
    }
}

