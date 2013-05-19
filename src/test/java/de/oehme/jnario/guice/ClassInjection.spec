package de.oehme.jnario.guice

import org.jnario.runner.CreateWith
import de.oehme.jnario.guice.uut.FooModule

@CreateWith(typeof(GuiceSpecCreator))
describe String "Class Injection"{

	context "without a module" {
		fact "the default constructor is used" {
			subject should be ""
		}
	}

	@InjectWith(typeof(FooModule))
	context "with a special module" {
		fact "the module takes precedence" {
			subject should be "Foo"
		}
	}
}